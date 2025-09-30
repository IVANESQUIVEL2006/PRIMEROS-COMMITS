class Termometro:
    MIN_C = -273.15
    MAX_C = 10000.0

    def __init__(self, celsius=0.0):
        self._celsius = None
        self.celsius = celsius

    @property
    def celsius(self): return self._celsius
    @celsius.setter
    def celsius(self, v):
        v = float(v)
        if v < self.MIN_C: raise ValueError("Menor al cero absoluto (-273.15°C)")
        if v > self.MAX_C: raise ValueError("Mayor al máximo permitido (10000°C)")
        self._celsius = v

    @property
    def fahrenheit(self): return self._celsius * 9/5 + 32
    @fahrenheit.setter
    def fahrenheit(self, v): self.celsius = (float(v) - 32) * 5/9


# Ejemplos
t = Termometro(25)
print(t.celsius, "°C =", t.fahrenheit, "°F")   # 25.0 °C = 77.0 °F
t.fahrenheit = 212
print(t.celsius, "°C")                         # 100.0 °C
try: t.celsius = -280
except Exception as e: print("Error:", e)
