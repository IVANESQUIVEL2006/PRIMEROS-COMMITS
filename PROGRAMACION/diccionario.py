def operacion_aritmetica():
    # Saludo con estilo
    print("🎉 Hola prro, ¿qué rollo? 🎉")
    
    # Pedimos los valores al usuario
    valor1 = float(input("✨ Dime el primer número, carnal: "))
    valor2 = float(input("🔥 Dime el segundo número, pa: "))
    
    # Preguntamos qué operación quiere realizar
    operacion = input("🎲 ¿Qué quieres hacer? (suma, resta, multiplicacion, division): ").lower()
    
    # Creamos el diccionario con los parámetros
    parametros = {
        "parametro1": valor1,
        "parametro2": valor2
    }
    
    # Inicializamos resultado como None por si no se define en los casos
    resultado = None
    
    # Realizamos la operación según la elección
    print("📡 Cámara pa, ahí te va el resultado:")
    if operacion == "suma":
        resultado = valor1 + valor2
        print(f"➕ La suma da: {resultado} 🎈")
    elif operacion == "resta":
        resultado = valor1 - valor2
        print(f"➖ La resta da: {resultado} 🎈")
    elif operacion == "multiplicacion":
        resultado = valor1 * valor2
        print(f"✖️ La multiplicación da: {resultado} 🎈")
    elif operacion == "division":
        if valor2 != 0:  # Verificamos que no se divida por cero
            resultado = valor1 / valor2
            print(f"➗ La división da: {resultado} 🎈")
        else:
            print("🚫 No se puede dividir por cero, prro!")
    else:
        print("❌ Esa operación no la cachamos, compa.")
    
    # Mostramos el diccionario con estilo
    print("📜 Diccionario de tus números, pa:", parametros)
    print("🎉 ¡Listo, prro! Nos vemos al rato 🐶")
    return resultado

# Llamamos a la función
operacion_aritmetica()
