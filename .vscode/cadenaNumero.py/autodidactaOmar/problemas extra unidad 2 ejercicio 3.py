class Puerta:
    def __init__(self, pin="1234"):
        self._abierta = False
        self._pin = pin
        self._intentos_fallidos = 0
        self._bloqueada = False

    # Propiedad para verificar si la puerta está abierta
    @property
    def abierta(self):
        return self._abierta

    @abierta.setter
    def abierta(self, valor):
        if self._bloqueada:
            raise Exception("Error: la Puerta está bloqueada")
        self._abierta = valor

    # Setter para cambiar el PIN
    @property
    def pin(self):
        return self._pin

    @pin.setter
    def pin(self, nuevo_pin):
        if len(nuevo_pin) != 4 or not nuevo_pin.isdigit():
            raise ValueError("El PIN debe tener 4 dígitos")
        self._pin = nuevo_pin

    # Método para abrir la puerta
    def abrir(self, pin_introducido):
        if self._bloqueada:
            print("¡Puerta bloqueada!")
            return
        if pin_introducido == self._pin:
            self._abierta = True
            self._intentos_fallidos = 0
            print("PIN correcto: puerta abierta")
        else:
            self._intentos_fallidos += 1
            intentos_restantes = 3 - self._intentos_fallidos
            if intentos_restantes == 0:
                self._bloqueada = True
                print("¡Puerta bloqueada!")
            else:
                print(f"PIN incorrecto: Intentos restantes: {intentos_restantes}")

# --- EJEMPLO DE USO ---
puerta = Puerta()

puerta.abrir("1111")  # PIN incorrecto
puerta.abrir("0000")  # PIN incorrecto
puerta.abrir("2222")  # tercer fallo -> puerta bloqueada
puerta.abrir("1234")  # intenta abrir cuando bloqueada -> mensaje de error
