# Clase Estudiante: representa a un estudiante inscrito en un curso
class Estudiante:
    # Constructor: inicializa los atributos del estudiante
    def __init__(self, nombre, numero_control):
        self.nombre = nombre                    # Guarda el nombre del estudiante
        self.numero_control = numero_control    # Guarda el número de control (Primary Key)

    # Método para mostrar los datos del estudiante
    def mostrar_datos(self):
        # Se usa f-string para imprimir los atributos del estudiante
        print(f"Nombre: {self.nombre}")
        print(f"Número de control: {self.numero_control}")

# Clase Curso: representa un curso con estudiantes inscritos
class Curso:
    # Constructor: inicializa el nombre del curso y la lista de estudiantes
    def __init__(self, nombre):
        self.nombre = nombre                    # Guarda el nombre del curso
        self.estudiantes = []                   # Lista vacía donde se guardarán los estudiantes

    # Método para inscribir un nuevo estudiante al curso
    def inscribir_estudiante(self, nombre, numero_control):
        nuevo_estudiante = Estudiante(nombre, numero_control)  # Se crea un nuevo objeto Estudiante

        # Se agrega el estudiante a la lista usando append()
        # append agrega el nuevo estudiante al final de la lista
        self.estudiantes.append(nuevo_estudiante)

    # Método para mostrar todos los estudiantes inscritos
    def mostrar_estudiantes(self):
        print(f"Estudiantes inscritos en el curso '{self.nombre}':")
        for estudiante in self.estudiantes:
            estudiante.mostrar_datos()
            print("---")  # Separador visual entre estudiantes

    # Método para contar cuántos estudiantes hay inscritos
    def contar_estudiantes(self):
        # len(self.estudiantes) cuenta cuántos estudiantes hay en la lista
        print(f"Total de estudiantes inscritos: {len(self.estudiantes)}")

# Aquí se crea el objeto curso usando la clase Curso
# Se guarda en la variable 'curso_redes' para poder usar sus métodos
curso_redes = Curso("Redes y Telecomunicaciones")

# Se inscriben dos estudiantes al curso usando el método inscribir_estudiante()
curso_redes.inscribir_estudiante("Jesús Iván Esquivel Ruiz", "20250001")
curso_redes.inscribir_estudiante("Ana López", "20250002")

# Se muestra la lista de estudiantes inscritos
curso_redes.mostrar_estudiantes()

# Se muestra el total de estudiantes inscritos
curso_redes.contar_estudiantes()