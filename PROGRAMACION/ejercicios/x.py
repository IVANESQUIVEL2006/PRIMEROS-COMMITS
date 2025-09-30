import os
from colorama import init, Fore, Style

# Inicializar colorama para colores en la terminal
init()

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_header():
    clear_screen()
    print(f"{Fore.CYAN}╔════════════════════════════════════╗{Style.RESET_ALL}")
    print(f"{Fore.CYAN}║    CALCULADORA DE FÍSICA 3000     ║{Style.RESET_ALL}")
    print(f"{Fore.CYAN}╚════════════════════════════════════╝{Style.RESET_ALL}")
    print(f"{Fore.GREEN}¡Hola, genio de la física! 👋✨{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}¿Qué vamos a calcular hoy? 😊🚀{Style.RESET_ALL}\n")

def calcular_velocidad():
    print(f"\n{Fore.MAGENTA}=== Calculando Velocidad (v = d/t) ==={Style.RESET_ALL}")
    try:
        distancia = float(input("Distancia (m): "))
        tiempo = float(input("Tiempo (s): "))
        velocidad = distancia / tiempo
        print(f"{Fore.GREEN}Velocidad = {velocidad:.2f} m/s 🎉{Style.RESET_ALL}")
    except ZeroDivisionError:
        print(f"{Fore.RED}¡Error! El tiempo no puede ser 0 😱{Style.RESET_ALL}")
    except ValueError:
        print(f"{Fore.RED}¡Ingresa números válidos, por favor! 🙏{Style.RESET_ALL}")

def calcular_fuerza():
    print(f"\n{Fore.MAGENTA}=== Calculando Fuerza (F = m × a) ==={Style.RESET_ALL}")
    try:
        masa = float(input("Masa (kg): "))
        aceleracion = float(input("Aceleración (m/s²): "))
        fuerza = masa * aceleracion
        print(f"{Fore.GREEN}Fuerza = {fuerza:.2f} N 💪{Style.RESET_ALL}")
    except ValueError:
        print(f"{Fore.RED}¡Ingresa números válidos, por favor! 🙏{Style.RESET_ALL}")

def calcular_energia_cinetica():
    print(f"\n{Fore.MAGENTA}=== Calculando Energía Cinética (Ec = ½mv²) ==={Style.RESET_ALL}")
    try:
        masa = float(input("Masa (kg): "))
        velocidad = float(input("Velocidad (m/s): "))
        energia = 0.5 * masa * (velocidad ** 2)
        print(f"{Fore.GREEN}Energía Cinética = {energia:.2f} J ⚡{Style.RESET_ALL}")
    except ValueError:
        print(f"{Fore.RED}¡Ingresa números válidos, por favor! 🙏{Style.RESET_ALL}")

def main():
    while True:
        print_header()
        print("1. Velocidad (v = d/t)")
        print("2. Fuerza (F = m × a)")
        print("3. Energía Cinética (Ec = ½mv²)")
        print("4. Salir")
        
        opcion = input(f"\n{Fore.YELLOW}Elige una opción (1-4): {Style.RESET_ALL}")
        
        if opcion == "1":
            calcular_velocidad()
        elif opcion == "2":
            calcular_fuerza()
        elif opcion == "3":
            calcular_energia_cinetica()
        elif opcion == "4":
            print(f"\n{Fore.CYAN}¡Adiós, físico estelar! 🌟 Hasta pronto 👋{Style.RESET_ALL}")
            break
        else:
            print(f"\n{Fore.RED}Opción no válida, intenta de nuevo 😅{Style.RESET_ALL}")
        
        input(f"\n{Fore.YELLOW}Presiona Enter para continuar...{Style.RESET_ALL}")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{Fore.CYAN}¡Nos vemos, calculador intrépido! 👾{Style.RESET_ALL}")
        