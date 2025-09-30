class Ecuacion1:
    def suma(self, a, b):
        return a + b

    def resta(self, a, b):
        return a - b

class Ecuacion2:
    def multiplicacion(self, a, b):
        return a * b

    def division(self, a, b):
        return a / b

class Resultado:
    def __init__(self):
        self.ecuacion1 = Ecuacion1()
        self.ecuacion2 = Ecuacion2()

# Crear instancia de Resultado
operacion = Resultado()

# Comprobación
print(operacion.ecuacion1.suma(10, 5))
print(operacion.ecuacion1.resta(10, 5))
print(operacion.ecuacion2.multiplicacion(10, 5))
print(operacion.ecuacion2.division(10, 5))

    


