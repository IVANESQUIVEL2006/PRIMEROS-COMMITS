class PuertaSegura:
    def __init__(self):
        self._abierta = False
        self._pin = "1234"  # PIN por defecto
        self.intentos_fallidos = 0
        self.bloqueada = False
    
    def intentar_abrir(self, pin):
        if self.bloqueada:
            return "¡Puerta bloqueada! (Demasiados intentos fallidos)"
        
        if pin == self._pin:
            self._abierta = True
            self.intentos_fallidos = 0
            return "PIN correcto. Puerta abierta."
        else:
            self.intentos_fallidos += 1
            intentos_restantes = 3 - self.intentos_fallidos
            
            if self.intentos_fallidos >= 3:
                self.bloqueada = True
                return "¡Puerta bloqueada por seguridad!"
            else:
                return f"PIN incorrecto. Intentos restantes: {intentos_restantes}"
    
    def cerrar_puerta(self):
        self._abierta = False
        return "Puerta cerrada."
    
    def estado_actual(self):
        return {
            "abierta": self._abierta,
            "bloqueada": self.bloqueada,
            "intentos_fallidos": self.intentos_fallidos
        }

# Función para mostrar el menú
def mostrar_menu():
    print("\n=== CONTROL DE ACCESO ===")
    print("1. Intentar abrir puerta")
    print("2. Cerrar puerta")
    print("3. Ver estado actual")
    print("4. Salir")
    try:
        opcion = int(input("Seleccione una opción (1-4): "))
        return opcion
    except ValueError:
        print("Por favor ingrese un número válido.")
        return -1

# Programa principal
def main():
    puerta = PuertaSegura()
    
    while True:
        opcion = mostrar_menu()
        
        if opcion == 1:
            if puerta.estado_actual()["bloqueada"]:
                print("La puerta está bloqueada. Contacte al administrador.")
            else:
                pin = input("Ingrese el PIN: ")
                resultado = puerta.intentar_abrir(pin)
                print(resultado)
        
        elif opcion == 2:
            resultado = puerta.cerrar_puerta()
            print(resultado)
        
        elif opcion == 3:
            estado = puerta.estado_actual()
            print("\n--- ESTADO ACTUAL ---")
            print(f"Abierta: {'Sí' if estado['abierta'] else 'No'}")
            print(f"Bloqueada: {'Sí' if estado['bloqueada'] else 'No'}")
            print(f"Intentos fallidos: {estado['intentos_fallidos']}/3")
        
        elif opcion == 4:
            print("Saliendo del sistema...")
            break
        
        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    main()
