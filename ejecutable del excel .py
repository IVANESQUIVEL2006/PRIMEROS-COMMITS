import os
import serial # Necesario para la comunicación serial
import time   # Necesario para las pausas (esperas)
import re     # Necesario para extraer datos con expresiones regulares

# ===============================================
# FUNCIONES AUXILIARES (Definiciones Requeridas)
# ===============================================

def send_command(ser, command, espera=0.5):
    """
    SIMULACIÓN: Envía un comando al dispositivo a través de la conexión serial.
    En una implementación real, esto interactuaría con ser.read() y ser.write().
    """
    if not ser:
        print(f"⚠️ Error: Conexión serial no válida para el comando: {command}")
        return "ERROR DE CONEXIÓN SIMULADO"
    
    # --- Lógica de simulación para evitar errores de ejecución ---
    
    # Simula la escritura y lectura
    # ser.write(command.encode('ascii') + b'\r') 
    time.sleep(espera) # Pausa para esperar la respuesta del dispositivo

    # Simulación de respuestas comunes para que el script no falle
    if command == "show version":
        # Respuesta simulada, ajusta el Serial para pruebas
        return "Cisco IOS Software, C800 Software (C800-UNIVERSALK9-M), Version 15.6(3)M1\nModel: Cisco 881\nProcessor board ID FHK12345678"
    if command == "write memory":
        return "Building configuration...\n[OK]"
    
    return "" # Respuesta vacía por defecto

def conectar_router(port):
    """
    SIMULACIÓN: Intenta establecer una conexión serial con el puerto dado.
    En una implementación real, esto devuelve un objeto serial.Serial.
    """
    print(f"🔗 Intentando conexión a {port}...")
    try:
        # Esto fallaría si no tienes el puerto COM real.
        # ser = serial.Serial(port, baudrate=9600, timeout=1) 
        
        # Simulamos una conexión exitosa para la prueba del script
        return port # Devolvemos el nombre del puerto como un objeto serial simulado
    except Exception as e:
        print(f"❌ No se pudo conectar a {port}. Error: {e}")
        return None

def extraer_datos(output):
    """
    SIMULACIÓN: Extrae el Modelo, Versión y Número de Serie del 'show version'.
    Debe usar re.search o re.findall para la lógica real.
    """
    # Lógica de extracción simulada basada en la respuesta de send_command:
    modelo_match = re.search(r"Model: (.*?)\n", output)
    version_match = re.search(r"Version (.*?)\n", output)
    serial_match = re.search(r"Processor board ID (\w+)", output)
    
    modelo = modelo_match.group(1).strip() if modelo_match else "DESCONOCIDO"
    version = version_match.group(1).strip() if version_match else "DESCONOCIDA"
    serial = serial_match.group(1).strip() if serial_match else "NODETECTADO"
    
    return modelo, version, serial

# ===============================================
# FUNCIÓN DE CONFIGURACIÓN MANUAL
# ===============================================
def configurar_dispositivo_manualmente(ser, fila):
    """
    Sustituye a 'configure_device'. Envía comandos de configuración
    al dispositivo a través de la conexión serial 'ser'.
    """
    
    DEVICE = fila.get("Device", "Router-Default")
    USER = fila.get("User", "cisco")
    PASSWORD = fila.get("Password", "cisco")
    IP_DOMAIN = fila.get("Ip-domain", "cisco.local")

    print(f"⚙️ Iniciando configuración manual para {DEVICE}...")

    # 1. Entrar en modo de configuración global
    send_command(ser, "configure terminal")
    
    # 2. Configurar el nombre del host (Hostname)
    send_command(ser, f"hostname {DEVICE}")

    # 3. Configurar usuario y contraseña
    send_command(ser, f"username {USER} privilege 15 secret {PASSWORD}")
    
    # 4. Configurar dominio IP (si aplica, útil para SSH/AAA)
    send_command(ser, f"ip domain name {IP_DOMAIN}")

    # 5. Cifrar contraseñas de texto plano
    send_command(ser, "service password-encryption")

    # 6. Salir y guardar configuración (write memory)
    send_command(ser, "end")
    output_save = send_command(ser, "write memory") 
    
    print(f"✔️ Configuración de Hostname y credenciales aplicada.")
    print(f"💾 Dispositivo guardado: {output_save.splitlines()[-1].strip()}")
    
    # Opcional: Volver al modo de ejecución privilegiada
    send_command(ser, "terminal length 0")


# ===============================================
# Función principal (Main Function)
# ===============================================
def procesar_csv(ruta_csv, ruta_resultados="routers_resultados.csv"):
    
    # 1. Preparación del CSV de entrada
    if not os.path.exists(ruta_csv):
        print(f"❌ El archivo '{ruta_csv}' no se encuentra. Se creará un archivo de ejemplo.")
        try:
            with open(ruta_csv, 'w', newline="", encoding="utf-8") as f:
                campos = ["Serie", "Port", "Device", "User", "Password", "Ip-domain", "Modelo", "Version"]
                writer = csv.DictWriter(f, fieldnames=campos)
                writer.writeheader()
                # Añade una fila de ejemplo (usa un puerto COM que tengas o simúlalo)
                writer.writerow({
                    "Serie": "FHK12345678", # Coincide con la simulación de show version
                    "Port": "COM3", 
                    "Device": "RTR-CORE-01",
                    "User": "admin",
                    "Password": "superpassword",
                    "Ip-domain": "global.net",
                    "Modelo": "Cisco 881", # Coincide para que la configuración se aplique
                    "Version": "15.6(3)M1" # Coincide para que la configuración se aplique
                })
            print(f"✅ Archivo '{ruta_csv}' de ejemplo creado. Edítalo y vuelve a ejecutar.")
        except Exception as e:
             print(f"⚠️ Error al crear archivo CSV: {e}")
        return

    # 2. Lectura del CSV de entrada
    with open(ruta_csv, newline="", encoding="utf-8") as f:
        lector = list(csv.DictReader(f))

    if not lector:
        print(f"ℹ El archivo '{ruta_csv}' está vacío. Terminando.")
        return

    resultados = []
    # Usamos set() para obtener puertos únicos
    puertos = set(row["Port"].strip() for row in lector if row.get("Port"))

    # 3. Procesamiento de cada puerto
    for port in puertos:
        print(f"\n=== Escaneando {port} ===")
        # En la simulación, 'ser' será el string del puerto
        ser = conectar_router(port) 
        if not ser:
            continue

        try:
            # En una implementación real, esto debe ser manejado por ser.write() y leer la respuesta
            send_command(ser, "terminal length 0") 
            salida = send_command(ser, "show version", espera=1.0)
            modelo, version, serial_detectado = extraer_datos(salida)

            print(f"🔎 Detectado en {port}: Serial={serial_detectado}, Modelo={modelo}, Versión={version}")

            # Buscamos la fila que coincide tanto por SERIAL como por PORT
            fila_coincidente = next((row for row in lector if row["Serie"].strip() == serial_detectado and row["Port"].strip() == port), None)

            # 4. Validación y Configuración
            if fila_coincidente:
                fila = fila_coincidente
                
                # Strip() para eliminar espacios en blanco que puedan causar fallos de coincidencia
                modelo_coincide = fila.get("Modelo","").strip() == modelo
                version_coincide = fila.get("Version","").strip() == version
                
                # Prepara la fila de resultados para el archivo de salida
                resultado_fila = {
                    "Serie": fila.get("Serie","N/A"),
                    "Port": fila.get("Port","N/A"),
                    "Device": fila.get("Device","Router"),
                    "User": fila.get("User","cisco"),
                    "Password": fila.get("Password","cisco"),
                    "Ip-domain": fila.get("Ip-domain","cisco.local"),
                    "Modelo": fila.get("Modelo","Desconocido_CSV"),
                    "Version": fila.get("Version","Desconocida_CSV"),
                    "Serie_detectada": serial_detectado,
                    "Modelo_detectado": modelo,
                    "Version_detectada": version,
                    "Modelo_coincide": "Sí" if modelo_coincide else "No",
                    "Version_coincide": "Sí" if version_coincide else "No"
                }
                
                if modelo_coincide and version_coincide:
                    print(f"✅ Coincidencia total. Aplicando configuración inicial a {fila['Device']}...")
                    
                    # Llamada a la función de configuración
                    configurar_dispositivo_manualmente(ser, fila)
                    
                    print(f"✅ Configuración completada y guardada en el dispositivo.")
                    
                else:
                    print(f"⚠ Coincidencia parcial (Modelo/Versión incorrecta en el CSV). No se aplica configuración.")
                
                resultados.append(resultado_fila)
            else:
                # Dispositivo no registrado (no coincide Serial y Puerto)
                print(f"❌ Dispositivo (Serial: {serial_detectado}) en {port} NO está registrado en CSV con ese puerto. Se omite configuración.")
                
                resultados.append({
                    "Serie": serial_detectado,
                    "Port": port,
                    "Device": "NO_REGISTRADO", 
                    "User": "N/A", "Password": "N/A", "Ip-domain": "N/A", "Modelo": "N/A", "Version": "N/A",
                    "Serie_detectada": serial_detectado,
                    "Modelo_detectado": modelo,
                    "Version_detectada": version,
                    "Modelo_coincide": "N/A",
                    "Version_coincide": "N/A"
                })


        except Exception as e:
            print(f"⚠️ Error procesando {port}: {e}")

        finally:
            # En la simulación, no hay un objeto serial real para cerrar
            if ser and isinstance(ser, str): # Solo cerramos si se simuló la conexión
                 print(f"🔌 Desconectando de {port}.")
            # ser.close() # Comentar si estás simulando y 'ser' no es un objeto serial.

    # 5. Guardar resultados
    if resultados:
        campos_base = ["Serie","Port","Device","User","Password","Ip-domain","Modelo","Version"]
        campos_detectados = ["Serie_detectada", "Modelo_detectado", "Version_detectada", "Modelo_coincide", "Version_coincide"]
        campos = campos_base + campos_detectados
        
        with open(ruta_resultados, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=campos)
            writer.writeheader()
            writer.writerows(resultados)
        print(f"\n✅ Resultados guardados en {ruta_resultados}")
    else:
        print("\nℹ No se obtuvieron resultados para guardar.")

# ===============================================
# Ejecutar script
# ===============================================
if __name__ == "__main__":
    procesar_csv("modelos.csv")