# Diccionario de funciones para operaciones matemáticas
def suma_dos(a, b):
    return a + b

def suma_mas(*args):
    return sum(args)

def resta(a, b):
    return a - b

def multiplica_dos(a, b):
    return a * b

def multiplica_mas(*args):
    resultado = 1
    for num in args:
        resultado *= num
    return resultado

def divide_mas(*args):
    resultado = args[0]
    for num in args[1:]:
        resultado /= num
    return resultado

# Diccionario con las operaciones
operaciones = {
    "1": ("➕ Suma de 2 números", suma_dos),
    "2": ("➕ Suma de más de 2 números", suma_mas),
    "3": ("➖ Resta de 2 números", resta),
    "4": ("✖️ Multiplicación de 2 números", multiplica_dos),
    "5": ("✖️ Multiplicación de más de 2 números", multiplica_mas),
    "6": ("➗ División de más de 2 números", divide_mas),
    "7": ("🚪 Salir", None)
}

# Programa principal
print("¡Qué tranza vato! 🌮 Cámara pa', te la lavas con este programa:")
print("¿Qué pedo, carnal? ¿Le vas a Chivas 🐐 o al América? 🦅")
print("Si le pones bolillo, carnal, ahí te va este menú bien chido:\n")

while True:
    # Mostrar menú
    for key, (desc, _) in operaciones.items():
        print(f"{key}. {desc}")
    
    opcion = input("\n¿Qué operación quieres, compa? (1-7): ")
    
    if opcion == "7":
        print("✌️ ¡Órale, nos vidrios, carnal! Que te vaya chido.")
        break
    
    if opcion not in operaciones:
        print("😵 ¡No mames, güey! Esa opción no existe. Échale otra vez.")
        continue
    
    desc, func = operaciones[opcion]
    print(f"\n🔢 Hiciste {desc}")
    
    # Pedir números según la operación
    try:
        if opcion in ["1", "3", "4"]:
            num1 = float(input("Dame el primer número, compa: "))
            num2 = float(input("Dame el segundo número, carnal: "))
            resultado = func(num1, num2)
        
        elif opcion in ["2", "5", "6"]:
            nums = input("Dame los números separados por espacio, vato: ").split()
            nums = [float(num) for num in nums]
            resultado = func(*nums)
        
        print(f"🎉 ¡Ahí te va, carnal! El resultado es: {resultado}")
    
    except ValueError:
        print("😡 ¡No seas gacho, güey! Pon números chidos, no letras.")
    except ZeroDivisionError:
        print("🤦‍♂️ ¡Qué pendejo, carnal! No se puede dividir entre cero.")
    
    print("───────────────────────")
