class Termometro:
    def __init__(self, temperatura=0):
        self._celsius = temperatura  # Valor inicial
    
    @property
    def celsius(self):
        """Obtiene la temperatura en Celsius"""
        return self._celsius
    
    @celsius.setter
    def celsius(self, valor):
        """Establece la temperatura en Celsius con validación"""
        if valor < -273.15 or valor > 10000:
            raise ValueError(f"Error: La temperatura {valor}°C no es válida. Debe estar entre -273.15°C y 10,000°C")
        self._celsius = valor
    
    @property
    def fahrenheit(self):
        """Obtiene la temperatura en Fahrenheit"""
        return (self._celsius * 9/5) + 32
    
    @fahrenheit.setter
    def fahrenheit(self, valor):
        """Establece la temperatura convirtiendo de Fahrenheit a Celsius"""
        celsius_temp = (valor - 32) * 5/9
        self.celsius = celsius_temp  # Usamos el setter de celsius para validar

# Pruebas del funcionamiento
if __name__ == "__main__":
    try:
        # Crear termómetro
        t = Termometro()
        
        # Prueba 1: Conversión básica
        t.celsius = 25
        print(f"25°C = {t.fahrenheit:.1f}°F")  # 25°C = 77.0°F
        
        # Prueba 2: Conversión inversa
        t.fahrenheit = 212
        print(f"212°F = {t.celsius:.1f}°C")  # 212°F = 100.0°C
        
        # Prueba 3: Temperatura inválida
        t.celsius = -280  # Esto debería lanzar un error
    except ValueError as e:
        print(e)