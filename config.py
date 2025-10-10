import serial 
import time   
import re     
import os
import sys
import pandas as pd # 👈 NUEVA LIBRERÍA
from typing import Dict, Any, List

# ==========================================================
# 1. FUNCIÓN DE LECTURA DE DATOS DEL ROUTER
# ==========================================================
def leer_datos_router_desde_excel(archivo_excel="routers.xlsx") -> List[Dict[str, Any]]:
    """
    Lee los datos de los routers desde un archivo de Excel (routers.xlsx).
    Retorna una lista de diccionarios, donde cada diccionario es un router.
    """
    if not os.path.exists(archivo_excel):
        print(f"❌ ERROR: Archivo '{archivo_excel}' no encontrado.")
        print("Cree un archivo de Excel con las columnas: Port, CLAVE_ENABLE, USER_CONSOLA, etc.")
        sys.exit(1)
        
    print(f"📄 Leyendo datos desde '{archivo_excel}'...")
    try:
        # Lee la primera hoja del archivo Excel
        df = pd.read_excel(archivo_excel)
        
        # Convierte el DataFrame a una lista de diccionarios
        datos_routers = df.to_dict('records')
        print(f"✅ Se cargaron {len(datos_routers)} routers.")
        return datos_routers
        
    except Exception as e:
        print(f"⚠️ Error al leer el archivo Excel: {e}")
        sys.exit(1)

# ==========================================================
# 2. FUNCIONES DE COMUNICACIÓN (MISMAS QUE TENÍAS)
# ==========================================================
# ... (Mantener 'read_until_idle', 'send_command', 'conectar_router' y 'modo_interactivo' tal cual) ...
def read_until_idle(ser, idle_timeout=2.0, overall_timeout=15):
    """Lee datos del puerto serial hasta que se detecta el prompt o inactividad."""
    # ... (cuerpo de la función) ...
    buf = bytearray()
    start = time.time()
    last = time.time()
    
    ser.write(b'\r\n')
    time.sleep(0.3) 

    while True:
        chunk = ser.read(1024)
        if chunk:
            buf.extend(chunk)
            last = time.time()
            if b'--More--' in chunk:
                ser.write(b' ')
                time.sleep(0.5)
            if buf.endswith(b'#') or buf.endswith(b'>') or b'Password:' in buf or b'password:' in buf or b'Username:' in buf:
                break
        else:
            if time.time() - last > idle_timeout: break
            if time.time() - start > overall_timeout: break
            time.sleep(0.1)
            
    return buf.decode(errors="ignore")

def send_command(ser, cmd, espera=1.0):
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
        print(f"❌ No se pudo abrir {port}: Verifica si el puerto está libre. Error: {e}")
        return None
    except Exception as e:
        print(f"⚠️ Error desconocido al conectar a {port}: {e}")
        return None

# Definición de 'modo_interactivo' (debe estar en el script)
def modo_interactivo(ser: serial.Serial):
    """
    Toma el control de la terminal para que el usuario escriba comandos.
    Se detiene cuando el usuario escribe 'exit'.
    """
    print("\n=======================================================")
    print("✅ MODO INTERACTIVO ACTIVO.")
    print("   Ahora puedes escribir comandos directamente al router.")
    print("   Cuando termines, escribe 'exit' para cerrar la conexión.")
    print("=======================================================")
    
    # Bucle para capturar la entrada del usuario y enviarla al router
    while True:
        try:
            # Muestra un prompt limpio para la entrada
            comando = input("CMD> ") 
            
            if comando.lower() == 'exit':
                break
            
            if not comando:
                continue

            # Envía el comando al router
            salida = send_command(ser, comando, espera=1.5)
            
            # Imprime la respuesta del router directamente
            print(salida.strip())
            
        except KeyboardInterrupt:
            # Permite salir con Ctrl+C
            break
        except Exception as e:
            print(f"\n[Error de comunicación]: {e}")
            break


# ==========================================================
# 3. FUNCIÓN PRINCIPAL DE AUTENTICACIÓN (MISMA QUE TENÍAS)
# ==========================================================
def autenticar(ser: serial.Serial, datos: Dict[str, str]):
    """Maneja la autenticación y pone el router en modo privilegiado (#)."""
    
    CLAVE_ENABLE = str(datos.get("CLAVE_ENABLE", "Cisco")) # Usamos .get y str() por si viene None de Excel
    USER_CONSOLA = str(datos.get("USER_CONSOLA", "cisco")) # Usamos .get y str() por si viene None de Excel
    
    ser.reset_input_buffer()
    ser.reset_output_buffer()

    # 1. Secuencia de escape y ENTERs (Salida del diálogo de configuración inicial)
    send_command(ser, "\r\n") 
    send_command(ser, "no", espera=1.5) 
    send_command(ser, "\r\n") 
    
    # 2. Lógica de Autenticación de CONSOLA/VTY (Si pide Username/Password)
    
    # Intento 1: Enviar USUARIO (si el prompt es 'Username:')
    salida_prompt = send_command(ser, USER_CONSOLA, espera=1.5)
    
    # Intento 2: Enviar CLAVE (Si el prompt es 'Password:' o falló el user)
    if "Password:" in salida_prompt or "password:" in salida_prompt:
        send_command(ser, CLAVE_ENABLE, espera=1.5) # Enviamos la clave de consola
        
    # 3. Entrar a modo privilegiado (ENABLE)
    salida_enable = send_command(ser, "enable", espera=2.5) 
    
    # 4. Enviar CLAVE DE ENABLE si el router lo pide (Re-autenticación)
    if "Password:" in salida_enable or "password:" in salida_enable:
          print(f"🔑 Enviando clave de ENABLE: {CLAVE_ENABLE}")
          salida_autenticacion = send_command(ser, CLAVE_ENABLE, espera=3.0) 
          
          if "Invalid" in salida_autenticacion or "login failed" in salida_autenticacion:
              print("❌ ERROR: Clave 'ENABLE' rechazada. ¡Verifica la clave!")
              raise Exception("Autenticación ENABLE fallida.")
    
    # 5. Desactiva paginación para la sesión manual
    send_command(ser, "terminal length 0")


# ==========================================================
# 4. FUNCIÓN PRINCIPAL (MODIFICADA PARA EXCEL)
# ==========================================================
def procesar_routers_desde_excel(archivo_excel="routers.xlsx"):
    """
    Función principal que itera sobre los routers leídos del Excel.
    """
    routers_a_procesar = leer_datos_router_desde_excel(archivo_excel)
    
    # NOTA: Este script solo procesa el PRIMER router en el Excel 
    # y entra en modo interactivo, imitando la lógica original.
    # Si quieres procesar TODOS, necesitarías cambiar 'modo_interactivo' 
    # por un conjunto de comandos automatizados (como 'show version').
    
    if not routers_a_procesar:
        print("No hay routers para procesar.")
        return
    
    datos_router = routers_a_procesar[0] # Tomamos solo el primer router
    port = str(datos_router.get("Port")) # Aseguramos que sea string

    if not port:
         print("❌ Error: La columna 'Port' no está definida para el primer router.")
         return

    print(f"\n=== Iniciando Proceso en Router: {datos_router.get('Device', 'Sin Nombre')} en {port} ===")
    ser = conectar_router(port) 
    
    if not ser:
        print("❌ Terminando proceso debido a fallo de conexión.")
        return

    try:
        # 1. Autenticar y elevar privilegios
        autenticar(ser, datos_router)
        
        # 2. Iniciar el modo de control manual
        modo_interactivo(ser)
        
        # OPCIONAL: Si quisieras ver la versión, harías esto en lugar de modo_interactivo:
        # print("Versión del Router:")
        # salida_version = send_command(ser, "show version")
        # print(salida_version)

    except Exception as e:
        print(f"⚠️ Error durante el proceso: {e}")

    finally:
        if ser:
            ser.close()
            print(f"🔌 Conexión cerrada.")


# ==========================================================
# 5. EJECUTAR SCRIPT
# ==========================================================
if __name__ == "__main__":
    procesar_routers_desde_excel("routers.xlsx")