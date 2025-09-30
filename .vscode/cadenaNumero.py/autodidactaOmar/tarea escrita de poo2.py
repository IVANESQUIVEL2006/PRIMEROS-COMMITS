# Clase Estudiante: representa a un estudiante con nombre y número de control
class Estudiante:
    def __init__(self, nombre, numero_control):
        # Atributos de la clase Estudiante
        self.nombre = nombre
        self.numero_control = numero_control

    def mostrar_datos(self):
        # Muestra en pantalla los datos del estudiante
        print(f"Número de control: {self.numero_control} | Nombre: {self.nombre}")


# Clase Curso: contiene una lista de estudiantes y métodos para gestionarlos
class Curso:
    def __init__(self, nombre_curso):
        # Nombre del curso
        self.nombre_curso = nombre_curso
        # Lista donde se guardan los estudiantes inscritos
        self.estudiantes = []

    def inscribir_estudiante(self, estudiante):
        # Agregar un estudiante a la lista
        self.estudiantes.append(estudiante)

    def mostrar_estudiantes(self):
        # Mostrar todos los estudiantes inscritos en el curso
        print(f" Curso: {self.nombre_curso}")
        for alumno in self.estudiantes:
            alumno.mostrar_datos()

    def contar_estudiantes(self):
        # Devuelve el número de estudiantes inscritos
        return len(self.estudiantes)

# pasamos a la ejecución
# Crear un curso
curso_de_cisco = Curso("curso_de_cisco")

# Crear estudiantes
est1 = Estudiante("Ivan Esquivel", "2403150031")
est2 = Estudiante("Jesus burciaga", "2403150044")
est3 = Estudiante("Ever Contreras", "2403150067")

# Inscribir estudiantes al curso
curso_de_cisco.inscribir_estudiante(est1)
curso_de_cisco.inscribir_estudiante(est2)
curso_de_cisco.inscribir_estudiante(est3)

# Mostrar los estudiantes del curso
curso_de_cisco.mostrar_estudiantes()

# Mostrar cuántos estudiantes hay inscritos
print(f"Total de estudiantes inscritos: {curso_de_cisco.contar_estudiantes()}")
