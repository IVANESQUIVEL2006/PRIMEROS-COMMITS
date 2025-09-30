import os
import csv
import serial 
import time   
import re     

# ==========================================================
# 1. EXPRESIONES REGULARES (REGEX)
# ==========================================================
REGEX_VERSION = re.compile(r"Version\s*[:]\s*([0-9A-Za-z\.\(\)\-_,]+)", re.IGNORECASE)
REGEX_SERIAL = re.compile(r"(?:System serial number|Processor board ID)\s*:\s*(\S+)", re.IGNORECASE)

# ==========================================================
# 2. FUNCIONES DE COMUNICACIÓN Y EXTRACCIÓN (REALES)
# ==========================================================

def read_until_idle(ser, idle_timeout=1.2, overall_timeout=10):
    """Lee datos del puerto serial hasta que el dispositivo deja de enviar."""
    buf = bytearray()
    start = time.time()
    last = time.time()
    ser.write(b'\r\n')
    time.sleep(0.5)

    while True:
        chunk = ser.read(1024)
        if chunk:
            buf.extend(chunk)
            last = time.time()
            if b'--More--' in chunk:
                ser.write(b' ')
                time.sleep(0.2)
            # Detecta el fin de la salida por el prompt
            if buf.endswith(b'>') or buf.endswith(b'#') or buf.endswith(b'Username:'):
                break
        else:
            if time.time() - last > idle_timeout: break
            if time.time() - start > overall_timeout: break
            time.sleep(0.05)
            
    return buf.decode(errors="ignore")

def send_command(ser, cmd, espera=0.3):
    """Envía comandos reales al dispositivo."""
    ser.write((cmd + "\r\n").encode())
    time.sleep(espera)
    return read_until_idle(ser)


def conectar_router(port, baudrate=9600):
    """Intenta establecer una conexión serial REAL."""
    print(f"🔗 Intentando conexión REAL a {port}...")
    try:
        ser = serial.Serial(port, baudrate, timeout=1, bytesize=8, parity='N', stopbits=1)
        ser.reset_input_buffer()
        ser.reset_output_buffer()
        print(f"🔗 Conexión exitosa a {port}.")
        return ser
    except serial.SerialException as e:
        print(f"❌ No se pudo abrir {port}: Verifica si el puerto está libre o el nombre es correcto. Error: {e}")
        return None
    except Exception as e:
        print(f"⚠️ Error desconocido al conectar a {port}: {e}")
        return None

def extraer_datos(salida):
    """Extrae el Modelo, Versión y Serial usando las REGEX."""
    modelo_match = re.search(r"Cisco\s*([A-Z0-9\-]+)", salida)
    modelo = modelo_match.group(1).strip() if modelo_match else "DESCONOCIDO_MODELO"
    m_ver = REGEX_VERSION.search(salida)
    version = m_ver.group(1).strip() if m_ver else "DESCONOCIDA"
    m_ser = REGEX_SERIAL.search(salida)
    serial = m_ser.group(1).strip() if m_ser else "NODETECTADO"
    return modelo, version, serial


# ==========================================================
# 3. FUNCIÓN DE CONFIGURACIÓN
# ==========================================================
def configurar_dispositivo(ser, fila):
    """Aplica la configuración básica al dispositivo usando los datos del CSV (fila)."""
    DEVICE = fila.get("Device", "Router-Default")
    USER = fila.get("User", "cisco")
    PASSWORD = fila.get("Password", "cisco")
    IP_DOMAIN = fila.get("Ip-domain", "cisco.local")

    print(f"⚙️ Iniciando configuración para {DEVICE}...")

    send_command(ser, "enable") 
    send_command(ser, "configure terminal")
    send_command(ser, f"hostname {DEVICE}")
    send_command(ser, f"username {USER} privilege 15 secret {PASSWORD}")
    send_command(ser, f"ip domain name {IP_DOMAIN}")
    send_command(ser, "service password-encryption")

    send_command(ser, "end")
    send_command(ser, "write memory", espera=5) 
    
    print(f"✔️ Configuración de Hostname y credenciales aplicada.")
    print(f"💾 Dispositivo guardado.")
    send_command(ser, "terminal length 0")


# ==========================================================
# 4. FUNCIÓN PRINCIPAL (MAIN FUNCTION)
# ==========================================================
def procesar_csv(ruta_csv, ruta_resultados="routers_resultados.csv"):
    
    # 💥 BLOQUE DE AUTOCREACIÓN DEL CSV 💥
    if not os.path.exists(ruta_csv):
        print(f"❌ El archivo '{ruta_csv}' no se encuentra. Creando plantilla de ejemplo...")
        try:
            with open(ruta_csv, 'w', newline="", encoding="utf-8") as f:
                campos = ["Serie", "Port", "Device", "User", "Password", "Ip-domain", "Modelo", "Version"]
                writer = csv.DictWriter(f, fieldnames=campos)
                writer.writeheader()
                
                # --- DATOS DE PLANTILLA ---
                writer.writerow({
                    "Serie": "REEMPLAZAR_CON_SERIAL_REAL", 
                    "Port": "COM3", 
                    "Device": "RTR-LAB-A",
                    "User": "admin",
                    "Password": "MiPassword123",
                    "Ip-domain": "practica.net",
                    "Modelo": "Cisco 1841", 
                    "Version": "12.4(24)T" 
                })
            print(f"✅ Archivo '{ruta_csv}' creado con datos de ejemplo.")
            print("🛑 AHORA: Edita ese archivo con los datos REALES de tu router (Serial, Port, Modelo) y vuelve a ejecutar.")
        except Exception as e:
             print(f"⚠️ Error al crear archivo CSV: {e}")
        return

    # Resto de la lógica (Lecura, Conexión, Configuración)
    # ... (El resto del código es idéntico al anterior) ...

    # 2. Lectura del CSV
    with open(ruta_csv, newline="", encoding="utf-8") as f:
        lector = list(csv.DictReader(f))

    if not lector:
        print(f"ℹ El archivo '{ruta_csv}' está vacío. Terminando.")
        return

    resultados = []
    puertos = set(row["Port"].strip() for row in lector if row.get("Port"))

    for port in puertos:
        print(f"\n=== Escaneando {port} ===")
        ser = conectar_router(port) 
        if not ser:
            continue

        try:
            send_command(ser, "\r\n")
            send_command(ser, "terminal length 0") 
            salida = send_command(ser, "show version", espera=3.0)
            modelo_detectado, version_detectada, serial_detectado = extraer_datos(salida)

            print(f"🔎 Detectado en {port}: Serial={serial_detectado}, Modelo={modelo_detectado}, Versión={version_detectada}")

            fila_coincidente = next((row for row in lector if row["Serie"].strip() == serial_detectado and row["Port"].strip() == port), None)

            if fila_coincidente:
                fila = fila_coincidente
                modelo_coincide = fila.get("Modelo","").strip() == modelo_detectado
                version_coincide = fila.get("Version","").strip() == version_detectada
                
                resultado_fila = {
                    **fila, 
                    "Serie_detectada": serial_detectado,
                    "Modelo_detectado": modelo_detectado,
                    "Version_detectada": version_detectada,
                    "Modelo_coincide": "Sí" if modelo_coincide else "No",
                    "Version_coincide": "Sí" if version_coincide else "No"
                }
                
                if modelo_coincide and version_coincide:
                    print(f"✅ Coincidencia total. Aplicando configuración a {fila['Device']}...")
                    configurar_dispositivo(ser, fila)
                    print(f"✅ Configuración finalizada.")
                else:
                    print(f"⚠ Coincidencia fallida. No se aplica configuración.")
                
                resultados.append(resultado_fila)
            else:
                print(f"❌ Serial {serial_detectado} detectado en {port} NO está registrado en el CSV. Se omite.")

        except Exception as e:
            print(f"⚠️ Error procesando {port} (revisar autenticación o estado del router): {e}")

        finally:
            if ser:
                ser.close()
                print(f"🔌 Conexión cerrada.")

    if resultados:
        campos = list(resultados[0].keys())
        with open(ruta_resultados, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=campos)
            writer.writeheader()
            writer.writerows(resultados)
        print(f"\n✅ Resultados de detección y validación guardados en {ruta_resultados}")
    else:
        print("\nℹ No se obtuvieron resultados para guardar.")

# ==========================================================
# 5. EJECUTAR SCRIPT
# ==========================================================
if __name__ == "__main__":
    procesar_csv("modelos.csv")