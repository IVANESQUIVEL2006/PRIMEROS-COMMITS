import pandas as pd
from netmiko import ConnectHandler
from netmiko.exceptions import NetMikoTimeoutException, NetMikoAuthenticationException
import re
from time import sleep
import sys
import os

# --- CONFIGURACIÓN DE CONEXIÓN Y ARCHIVOS ---
CSV_FILE_OUT = 'router_interfaces_status.csv'
ROUTER_NAME = "RFJC2047A07L" 
LOG_FILE = "netmiko_session.log" 

# ⚠️ ¡ATENCIÓN! Se ha eliminado el 'secret' para la prueba final.
# La conexión se hará solo con USUARIO y PASSWORD.
ENABLE_SECRET = "" 

# Configuración de Conexión Serial
router_info = {
    "device_type": "cisco_ios", 
    "host": "COM3", 
    "username": "cisco", 
    "password": "Cisco",
    "secret": None,                   # Se elimina la clave 'secret'
    "port": 9600, 
    "session_log": LOG_FILE, 
    "timeout": 30,                    # Tiempo de espera extendido
}

# --- FUNCIONES DE LECTURA Y PARSEO ---

def parse_interfaces(output):
    """Convierte la salida de 'show ip interface brief' en un DataFrame."""
    interface_data = []
    lines = output.strip().splitlines()
    start_index = 0
    for i, line in enumerate(lines):
        if 'Interface' in line and 'IP-Address' in line:
            start_index = i + 1
            break
            
    for line in lines[start_index:]:
        if line.strip(): 
            match = re.match(r'(\S+)\s+(\S+)\s+(\S+)\s+(\S+)\s+(\S+)\s+(\S+)', line)
            if match:
                data = match.groups()
                interface_data.append({
                    'Interface': data[0],
                    'IP_Address': data[1],
                    'Status_Layer1': data[4],
                    'Protocol_Layer2': data[5],
                })
    return interface_data

def show_command_live(net_connect):
    """Permite al usuario mandar comandos SHOW manualmente."""
    while True:
        comando = input(f"\n[{ROUTER_NAME}#] COMANDO SHOW ('exit' para menú): ").strip()
        if comando.lower() in ['exit', 'quit']:
            break
        if comando:
            if not comando.lower().startswith('show'):
                print("❌ ERROR: Solo comandos que inician con 'show'.")
                continue
            try:
                print(f"--- Resultado de: {comando} ---")
                output = net_connect.send_command(comando)
                print(output)
            except Exception as e:
                print(f"❌ Error al ejecutar comando: {e}")

def live_config_mode(net_connect):
    """Permite al usuario ingresar comandos de configuración y guardarlos."""
    print("\n==================== MODO CONFIGURACIÓN ====================")
    print("⚠️ Escribe 'END' para salir del modo conf. Escribe 'SAVE' para GUARDAR y salir.")
    
    config_commands = []
    
    while True:
        user_input = input(f"[{ROUTER_NAME}(config)#] ").strip()
        
        if user_input.upper() == 'END':
            break
        
        if user_input.upper() == 'SAVE':
            print("\n💾 Aplicando y guardando configuración...")
            try:
                net_connect.send_config_set(config_commands) 
                net_connect.send_command("write memory")
                print("✅ Configuración guardada con éxito.")
            except Exception as e:
                print(f"❌ Error al guardar configuración: {e}")
            return

        if user_input:
            config_commands.append(user_input)
            print(f"   [COMANDO AÑADIDO: {user_input}]")


# --- MENÚ PRINCIPAL Y LÓGICA DE CONEXIÓN ---

def print_menu():
    """Muestra el menú principal."""
    print("\n================== MENÚ PRINCIPAL PERROTA ==================")
    print("1. 🚨 **Diagnóstico y Exportar** a CSV (Automático)")
    print("2. ✍️ **Configuración en Vivo** (Modificar y Guardar)")
    print("3. 🔍 **Comandos Manuales** (Solo SHOW)")
    print("4. 🚪 Salir")
    print("============================================================")

def execute_diagnostics_and_export(net_connect):
    """Ejecuta el diagnóstico y la exportación a CSV."""
    
    # 1. Ejecutar y mostrar diagnóstico
    print("\n--- 🚨 DIAGNÓSTICO AUTOMÁTICO ---")
    commands = ["show version | include IOS|uptime", "show clock", "show ip interface brief"]
    output_set = net_connect.send_command_set(commands)
    
    # Imprimir diagnóstico
    print('\n'.join(output_set))
    
    # 2. Leer interfaces para CSV
    output_interfaces = output_set[-1] 
    datos_interfaces = parse_interfaces(output_interfaces)
    
    # 3. Exportar
    if datos_interfaces:
        df = pd.DataFrame(datos_interfaces)
        csv_path = os.path.join(os.getcwd(), CSV_FILE_OUT)
        df.to_csv(csv_path, index=False)
        print(f"\n🎉 ÉXITO: Datos de {len(df)} interfaces guardados en '{csv_path}'")
    else:
        print("🔴 No se encontraron interfaces con IP asignada para exportar.")


def main_program():
    net_connect = None
    try:
        print(f"[*] Intentando conectar automáticamente a {router_info['host']}...")
        
        # 1. Conexión
        # Conexión sin la clave 'secret'
        net_connect = ConnectHandler(**router_info)
        
        # Como eliminamos el 'secret', intentamos el 'enable' sin contraseña.
        # Si el router lo pide, esto fallará, indicando que el 'secret' es obligatorio.
        net_connect.enable() 
        
        print(f"✅ Conexión serial exitosa al {net_connect.base_prompt}!")

        # 2. **EJECUCIÓN AUTOMÁTICA DE DIAGNÓSTICO Y CSV**
        execute_diagnostics_and_export(net_connect)

        # 3. Bucle del Menú
        while True:
            print_menu()
            choice = input("Selecciona una opción (1-4): ").strip()

            if choice == '1':
                execute_diagnostics_and_export(net_connect) 

            elif choice == '2':
                live_config_mode(net_connect)

            elif choice == '3':
                show_command_live(net_connect)
            
            elif choice == '4':
                print("👋 Cerrando conexión y saliendo. ¡Adiós!")
                break
            
            else:
                print("❌ Opción no válida. Intenta de nuevo.")

    except NetMikoAuthenticationException as e:
        print(f"\n[!] ERROR: Fallo de Autenticación. La contraseña de 'enable' es OBLIGATORIA.")
        print("   Vuelve a configurar ENABLE_SECRET con la contraseña correcta.")
        sys.exit(1)
    except Exception as e:
        print(f"\n[!] ERROR CRÍTICO. El puerto COM3 está BLOQUEADO.")
        print(f"   Asegúrate de liberar el puerto usando PowerShell (el método diferente) antes de ejecutar.")
        print(f"   Mensaje de error: {e}")
        sys.exit(1)
    finally:
        if net_connect:
            net_connect.disconnect()

if __name__ == "__main__":
    main_program()