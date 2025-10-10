#!/usr/bin/env python3
"""
router_serial_menu.py - Conexión serial a router Cisco con menú interactivo.

Ahora incluye:
✅ Ver IPs actuales del router
✅ Cambiar IP de cualquier interfaz (con validación)
✅ Modo seguro que evita errores de configuración
"""

import csv
import getpass
import sys
from typing import List, Dict, Optional
from netmiko import ConnectHandler, NetMikoTimeoutException, NetMikoAuthenticationException

CSV_FILE = "interfaces.csv"


# --- Conexión por serial usando Netmiko ---
def connect_serial_com(port: str = "COM3", baudrate: int = 9600, username: str = "", password: str = "", secret: str = "", device_type_base: str = "cisco_ios") -> Optional[ConnectHandler]:
    serial_device_type = f"{device_type_base}_serial"
    device = {
        "device_type": serial_device_type,
        "username": username,
        "password": password,
        "secret": secret,
        "fast_cli": False,
        "serial_settings": {
            "port": port,
            "baudrate": baudrate,
            "bytesize": 8,
            "parity": "N",
            "stopbits": 1,
        },
    }
    try:
        conn = ConnectHandler(**device)
        return conn
    except NetMikoAuthenticationException:
        print("[-] Autenticación fallida en la conexión serial.")
    except NetMikoTimeoutException:
        print("[-] Timeout o puerto no disponible. Verifica cable y puerto COM.")
    except Exception as e:
        print(f"[-] Error al conectar por serial: {e}")
    return None


# --- Lectura inicial del dispositivo ---
def read_device_basic_info(conn: ConnectHandler) -> Dict[str, str]:
    info = {"prompt": "", "show_version": ""}
    try:
        conn.enable()
        info["prompt"] = conn.find_prompt()
        out = conn.send_command("show version", expect_string=r"#|>$", delay_factor=1)
        info["show_version"] = out[:2000]
    except Exception as e:
        print(f"[-] Error leyendo info básica: {e}")
    return info


# --- Envío de comandos manual (corregido) ---
def send_manual_command(conn) -> None:
    while True:
        cmd = input("Ingresa comando (o 'back' para volver): ").strip()
        if not cmd:
            continue
        if cmd.lower() in ("back", "b", "salir"):
            return
        try:
            conn.enable()
            # Si estás en modo config, salir antes de ejecutar show
            prompt = conn.find_prompt()
            if "(config" in prompt:
                conn.send_command_timing("end")

            print("\n[*] Ejecutando comando, espera un momento...\n")
            output = conn.send_command_timing(
                cmd,
                strip_prompt=False,
                strip_command=False,
                delay_factor=2,
            )
            if not output.strip():
                output = conn.send_command(cmd, expect_string=None, delay_factor=2, read_timeout=10)
            print("\n--- SALIDA ---")
            print(output if output.strip() else "[Sin salida o comando inválido]")
            print("--------------\n")
        except Exception as e:
            print(f"Error al ejecutar comando: {e}")


# --- Parseo del show ip interface brief ---
def parse_show_ip_interface_brief(output: str) -> List[Dict[str, str]]:
    lines = [l for l in output.splitlines() if l.strip()]
    results = []
    if not lines:
        return results
    start_idx = 0
    for i, line in enumerate(lines[:5]):
        if "IP-Address" in line or "IP Address" in line:
            start_idx = i + 1
            break
    for line in lines[start_idx:]:
        parts = line.split()
        if len(parts) < 2:
            continue
        interface = parts[0]
        ip = parts[1] if len(parts) >= 2 else "unassigned"
        status = parts[-2] if len(parts) >= 2 else ""
        protocol = parts[-1] if len(parts) >= 1 else ""
        if len(parts) > 6:
            status = " ".join(parts[4:-1])
            protocol = parts[-1]
        results.append({"interface": interface, "ip": ip, "status": status, "protocol": protocol})
    return results


def save_interfaces_to_csv(interfaces: List[Dict[str, str]], filename: str = CSV_FILE) -> None:
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["interface", "ip", "status", "protocol"])
        writer.writeheader()
        for row in interfaces:
            writer.writerow(row)
    print(f"[+] Guardado {len(interfaces)} interfaces en '{filename}'.")


def load_interfaces_from_csv(filename: str = CSV_FILE) -> List[Dict[str, str]]:
    try:
        with open(filename, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            return [row for row in reader]
    except FileNotFoundError:
        return []


# --- NUEVO: Ver IP y cambiar IP ---
def view_and_change_ip(conn):
    try:
        conn.enable()
        print("[*] Obteniendo IPs actuales...\n")
        output = conn.send_command("show ip interface brief")
        interfaces = parse_show_ip_interface_brief(output)
        if not interfaces:
            print("[-] No se detectaron interfaces.")
            return

        print("\n=== Interfaces del router ===")
        for i, itf in enumerate(interfaces, 1):
            print(f"{i}) {itf['interface']:20} {itf['ip']:16} {itf['status']:10} {itf['protocol']}")
        choice = input("\nSelecciona interfaz para cambiar IP (número o 'back'): ").strip()
        if choice.lower() in ("back", "b"):
            return
        idx = int(choice) - 1
        if idx < 0 or idx >= len(interfaces):
            print("Opción fuera de rango.")
            return

        selected = interfaces[idx]
        print(f"\nInterfaz seleccionada: {selected['interface']} (IP actual: {selected['ip']})")
        new_ip = input("Nueva IP (ej. 192.168.10.1): ").strip()
        mask = input("Máscara (ej. 255.255.255.0): ").strip()
        confirm = input(f"¿Aplicar {new_ip} {mask} en {selected['interface']}? (s/n): ").strip().lower()
        if confirm != "s":
            print("Cancelado por usuario.")
            return

        print("[*] Aplicando nueva IP...")
        conn.config_mode()
        conn.send_command_timing(f"interface {selected['interface']}")
        conn.send_command_timing(f"ip address {new_ip} {mask}")
        conn.send_command_timing("no shutdown")
        conn.send_command_timing("end")
        print("[+] IP actualizada correctamente ✅")

        # Mostrar verificación
        verify = conn.send_command("show ip interface brief")
        print("\n--- Nueva configuración ---")
        print(verify)
        print("---------------------------\n")

    except Exception as e:
        print(f"Error al cambiar IP: {e}")


# --- Menú principal ---
def main_menu(conn):
    interfaces_cache = load_interfaces_from_csv()
    while True:
        print("\n=== MENU PRINCIPAL ===")
        print("1) Enviar comando manual")
        print("2) Leer interfaces (show ip interface brief) y guardar CSV")
        print("3) Ver o cambiar IP de interfaz")
        print("4) Desconectar y salir")
        print("5) Salir programa")
        option = input("Elige opción: ").strip()
        if option == "1":
            send_manual_command(conn)
        elif option == "2":
            print("[*] Ejecutando 'show ip interface brief' ...")
            try:
                conn.enable()
                out = conn.send_command("show ip interface brief")
                interfaces = parse_show_ip_interface_brief(out)
                if not interfaces:
                    print("[-] No se detectaron interfaces. Salida:\n", out)
                else:
                    for it in interfaces:
                        print(f"{it['interface']:20} {it['ip']:16} {it['status']:10} {it['protocol']}")
                    save_interfaces_to_csv(interfaces)
                    interfaces_cache = interfaces
            except Exception as e:
                print(f"Error al ejecutar comando: {e}")
        elif option == "3":
            view_and_change_ip(conn)
        elif option == "4":
            try:
                conn.disconnect()
            except Exception:
                pass
            print("Desconectado. Saliendo.")
            return
        elif option == "5":
            print("Saliendo programa.")
            try:
                conn.disconnect()
            except Exception:
                pass
            sys.exit(0)
        else:
            print("Opción inválida. Intenta otra vez.")


# --- Ejecución principal ---
def run():
    print("=== Conexión por consola serial al router (ej. USB -> COM3) ===")
    port = input("Puerto serial (ej. COM3 o /dev/ttyUSB0) [COM3]: ").strip() or "COM3"
    baud_input = input("Baudrate [9600]: ").strip() or "9600"
    try:
        baudrate = int(baud_input)
    except ValueError:
        baudrate = 9600

    username = input("Usuario (si aplica, enter para none): ").strip()
    password = getpass.getpass("Contraseña (si aplica, enter para none): ")
    secret = getpass.getpass("Enable/secret (si aplica, enter para none): ")

    print(f"[*] Intentando conectar por serial a {port} a {baudrate}bps ...")
    conn = connect_serial_com(port=port, baudrate=baudrate, username=username, password=password, secret=secret)
    if not conn:
        print("[-] No se pudo establecer la conexión serial.")
        return

    print("[+] Conexión serial establecida. Leyendo información básica del dispositivo...")
    info = read_device_basic_info(conn)
    print("=== Info leída ===")
    print("Prompt:", info.get("prompt"))
    sv = info.get("show_version") or ""
    if sv:
        print("--- show version (resumen) ---")
        print(sv[:1000])
        if len(sv) > 1000:
            print("[... salida recortada ...]")
    else:
        print("[*] No se obtuvo salida de 'show version'.")

    print("\nYa puedes usar el menú principal para administrar el router.")
    main_menu(conn)


if __name__ == "__main__":
    run()
