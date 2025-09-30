import pandas as pd
from netmiko import ConnectHandler
import getpass # Para pedir la contraseña de forma segura

# --- Configuración Inicial ---
ARCHIVO_EXCEL = 'dispositivos.xlsx' 
# El archivo debe tener las columnas: host, device_type, username, password, enable_secret
# (Asegúrate de que 'dispositivos.xlsx' está en la misma carpeta)

# ----------------------------------------------------------------------
## Función Principal para Configuración por Consola
# ----------------------------------------------------------------------

def configurar_dispositivos_por_consola():
    """
    Lee los dispositivos del Excel, pide comandos al usuario por consola 
    y los aplica en modo configuración a todos los dispositivos.
    """
    try:
        # 1. Leer el archivo de Excel y cargar los dispositivos
        df = pd.read_excel(ARCHIVO_EXCEL)
        devices_to_configure = df.to_dict('records') # Convertir DataFrame a lista de diccionarios
        print(f"✅ Archivo '{ARCHIVO_EXCEL}' cargado con {len(devices_to_configure)} dispositivos.")
        
    except FileNotFoundError:
        print(f"❌ ERROR: No se encontró el archivo '{ARCHIVO_EXCEL}'. Asegúrate de que esté en esta carpeta.")
        return
    except Exception as e:
        print(f"❌ Ocurrió un error al leer el Excel: {e}")
        return

    # 2. Pedir los comandos de configuración al usuario
    print("\n--- Modo de Configuración ---")
    print("Ingresa los comandos que deseas enviar (uno por línea).")
    print("Cuando termines, escribe 'FIN' y presiona Enter.")
    
    comandos = []
    while True:
        linea = input("> ")
        if linea.upper() == 'FIN':
            break
        comandos.append(linea)

    if not comandos:
        print("🛑 No se ingresó ningún comando. Cancelando operación.")
        return

    print(f"\nSe enviarán {len(comandos)} comandos de configuración a todos los dispositivos.")
    print("Comandos a enviar:")
    for cmd in comandos:
        print(f"  - {cmd}")
    print("-" * 50)
    
    
    # 3. Iterar y aplicar la configuración
    for device in devices_to_configure:
        
        # Netmiko espera un diccionario, y el DataFrame ya nos dio eso.
        # Solo aseguramos que el puerto es 22 por defecto si no está en el Excel
        if 'port' not in device:
             device['port'] = 22

        print(f"\n--- Conectando a {device['host']} ({device['device_type']})...")

        try:
            # 4. Establecer la conexión
            net_connect = ConnectHandler(**device)
            print(f"✅ Conexión establecida. Aplicando configuración...")
            
            # 5. Enviar los comandos de configuración
            # send_config_set() se encarga de entrar en modo 'conf t' y salir.
            output = net_connect.send_config_set(comandos)
            
            # 6. Imprimir el resultado de la configuración
            print("--- Respuesta del Dispositivo ---")
            print(output)
            print("---------------------------------")
            
            # 7. Cerrar la conexión
            net_connect.disconnect()
            
        except Exception as e:
            print(f"❌ Falló la conexión o la configuración con {device['host']}: {e}")

    print("\n✨ Proceso de configuración masiva finalizado.")
    
# ----------------------------------------------------------------------
## Ejecución del Script
# ----------------------------------------------------------------------

if __name__ == "__main__":
    configurar_dispositivos_por_consola()
