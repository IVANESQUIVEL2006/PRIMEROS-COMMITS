# Importamos la librería 'functools' para usar el decorador 'wraps'
import functools

# Definimos una clase principal llamada 'HerramientasNumericas' para agrupar todas las funcionalidades
class HerramientasNumericas:
    """
    Esta clase contiene métodos para realizar diversas operaciones numéricas y de validación.
    Incluye conversiones entre números enteros y romanos, validación de paréntesis,
    obtención de subconjuntos y verificación de divisibilidad.
    """

    # Definimos un decorador simple para registrar la llamada a los métodos
    def registrador(func):
        """
        Este decorador imprime un mensaje antes de ejecutar un método,
        indicando cuál función está a punto de ser llamada.
        """
        @functools.wraps(func)
        def envoltura(*args, **kwargs):
            # Imprime el nombre de la función que se va a ejecutar
            print(f"Llamando al método: {func.__name__}")
            # Ejecuta la función original y almacena el resultado
            resultado = func(*args, **kwargs)
            # Retorna el resultado de la función
            return resultado
        return envoltura

    @registrador
    def entero_a_romano(self, num):
        """
        Convierte un número entero a su representación en números romanos.
        Utiliza un diccionario para mapear los valores de los números romanos.

        Args:
            num (int): El número entero que se desea convertir. Debe ser un entero positivo.

        Returns:
            str: La representación en números romanos del entero dado.

        Raises:
            ValueError: Si el número no es un entero positivo o está fuera del rango de conversión.
        """
        if not isinstance(num, int) or num <= 0:
            raise ValueError("El número debe ser un entero positivo.")

        # Diccionario que mapea los valores enteros a sus símbolos romanos correspondientes
        valores = [
            (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"), (100, "C"),
            (90, "XC"), (50, "L"), (40, "XL"), (10, "X"), (9, "IX"), (5, "V"),
            (4, "IV"), (1, "I")
        ]
        
        resultado = ""  # Inicializamos una cadena vacía para construir el resultado
        for valor, simbolo in valores:
            # Mientras el número sea mayor o igual al valor actual, agregamos el símbolo al resultado
            while num >= valor:
                resultado += simbolo
                num -= valor  # Restamos el valor al número para continuar con el siguiente
        return resultado

    @registrador
    def romano_a_entero(self, s):
        """
        Convierte un número romano a su representación en número entero.
        Maneja la lógica de la notación sustractiva (ej. IV = 4).

        Args:
            s (str): La cadena que contiene el número romano.

        Returns:
            int: El número entero que corresponde al número romano.
        """
        # Diccionario que mapea los símbolos romanos a sus valores enteros
        romanos_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        
        entero_total = 0  # Inicializamos la suma total
        i = 0  # Inicializamos el índice para recorrer la cadena
        while i < len(s):
            # Obtenemos el valor del carácter actual
            valor_actual = romanos_map[s[i]]
            # Verificamos si hay un siguiente carácter para la notación sustractiva
            if i + 1 < len(s):
                valor_siguiente = romanos_map[s[i+1]]
                # Si el valor actual es menor que el siguiente, restamos el valor actual
                if valor_actual < valor_siguiente:
                    entero_total += valor_siguiente - valor_actual
                    i += 2  # Saltamos dos posiciones porque ya procesamos dos caracteres
                else:
                    # Si no es sustractivo, sumamos el valor actual
                    entero_total += valor_actual
                    i += 1  # Avanzamos una posición
            else:
                # Si es el último carácter, simplemente sumamos su valor
                entero_total += valor_actual
                i += 1
        return entero_total

    @registrador
    def validar_parentesis(self, s):
        """
        Verifica la validez de una cadena que contiene paréntesis '()', corchetes '[]' y llaves '{}'.
        Utiliza una pila (lista) para verificar el orden de apertura y cierre.

        Args:
            s (str): La cadena de paréntesis a validar.

        Returns:
            bool: True si la cadena es válida, False en caso contrario.
        """
        # Pila para almacenar los paréntesis de apertura
        pila = []
        # Diccionario que mapea los paréntesis de cierre a sus correspondientes de apertura
        mapeo = {")": "(", "]": "[", "}": "{"}
        
        for char in s:
            # Si el carácter es un paréntesis de apertura, lo agregamos a la pila
            if char in mapeo.values():
                pila.append(char)
            # Si es un paréntesis de cierre
            elif char in mapeo.keys():
                # Si la pila está vacía o el último elemento no coincide, es inválido
                if not pila or mapeo[char] != pila.pop():
                    return False
            # Si el carácter no es un paréntesis, se puede ignorar o manejar como error
            # Para este caso, asumimos que solo se dan paréntesis
        
        # La cadena es válida si y solo si la pila queda vacía al final
        return not pila

    @registrador
    def encontrar_subconjuntos(self, nums):
        """
        Obtiene todos los subconjuntos únicos de un conjunto de números enteros distintos.
        Utiliza un enfoque recursivo con 'backtracking'.

        Args:
            nums (list): Una lista de números enteros distintos.

        Returns:
            list: Una lista de listas que contiene todos los subconjuntos posibles.
        """
        # Lista principal que almacenará todos los subconjuntos
        subconjuntos = [[]]
        
        for num in nums:
            # Para cada número en la lista original, creamos nuevos subconjuntos
            # Añadiendo el número a cada subconjunto ya existente
            subconjuntos.extend([subconjunto + [num] for subconjunto in subconjuntos])
            
        return subconjuntos
    
    @registrador
    def verificar_divisibilidad(self, numeros):
        """
        Determina qué números de una lista son divisibles por 2, 3 y 5.
        La función solo procesa números mayores a 10.

        Args:
            numeros (list): Una lista de 5 números enteros mayores a 10.

        Returns:
            dict: Un diccionario donde las claves son los números y los valores
                  son una lista de los divisores (2, 3, 5) a los que el número
                  es divisible.
        """
        resultados = {}  # Diccionario para almacenar los resultados
        
        # Validamos que la lista contenga exactamente 5 números
        if len(numeros) != 5:
            raise ValueError("Debe ingresar exactamente 5 números.")
        
        # Validamos que todos los números sean mayores a 10
        if not all(num > 10 for num in numeros):
            raise ValueError("Todos los números deben ser mayores a 10.")
            
        for num in numeros:
            divisibles = []  # Lista temporal para guardar los divisores de cada número
            if num % 2 == 0:
                divisibles.append(2)
            if num % 3 == 0:
                divisibles.append(3)
            if num % 5 == 0:
                divisibles.append(5)
            # Almacenamos el resultado en el diccionario, asociando el número con sus divisores
            resultados[num] = divisibles
            
        return resultados

# ---
# Ejemplo de uso de la clase y sus métodos
if __name__ == "__main__":
    # Creamos una instancia de la clase 'HerramientasNumericas'
    h = HerramientasNumericas()
    
    print("--- Conversión de entero a romano ---")
    # Convertimos el número 1994 a romano
    numero_entero = 1994
    romano = h.entero_a_romano(numero_entero)
    print(f"El número {numero_entero} en romano es: {romano}")
    
    print("\n--- Conversión de romano a entero ---")
    # Convertimos el número romano 'MCMXCIV' a entero
    numero_romano = "MCMXCIV"
    entero = h.romano_a_entero(numero_romano)
    print(f"El número romano {numero_romano} en entero es: {entero}")

    print("\n--- Validación de paréntesis ---")
    # Validamos una cadena de paréntesis válida
    cadena_valida = "()[]{}"
    print(f"'{cadena_valida}' es válida: {h.validar_parentesis(cadena_valida)}")
    # Validamos una cadena de paréntesis inválida
    cadena_invalida = "({[)]}"
    print(f"'{cadena_invalida}' es válida: {h.validar_parentesis(cadena_invalida)}")
    
    print("\n--- Obtención de subconjuntos ---")
    # Creamos una lista de números para encontrar sus subconjuntos
    conjunto_numeros = [4, 5, 6]
    subconjuntos_obtenidos = h.encontrar_subconjuntos(conjunto_numeros)
    print(f"Subconjuntos de {conjunto_numeros}: {subconjuntos_obtenidos}")

    print("\n--- Verificación de divisibilidad ---")
    # Creamos una lista de 5 números mayores a 10
    numeros_divisibilidad = [12, 15, 20, 21, 30]
    divisibles = h.verificar_divisibilidad(numeros_divisibilidad)
    print(f"Divisibilidad de los números {numeros_divisibilidad}: {divisibles}")