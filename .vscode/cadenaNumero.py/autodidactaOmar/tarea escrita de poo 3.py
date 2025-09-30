class Libro:
    def __init__(self, titulo, autor, año):
        # Atributos principales del libro
        self.titulo = titulo
        self.autor = autor
        self.año = año
        self.prestado = False  # Por defecto, el libro está disponible

    def marcar_prestado(self):
        # Cambiar el estado del libro a prestado
        self.prestado = True

    def marcar_devuelto(self):
        # Cambiar el estado del libro a disponible
        self.prestado = False

    def mostrar_info(self):
        # Mostrar información del libro
        estado = "Prestado" if self.prestado else "Disponible"
        print(f"Título: {self.titulo} | Autor: {self.autor} | Año: {self.año} | Estado: {estado}")


# Clase Alumno: representa a un alumno de la escuela
class Alumno:
    def __init__(self, nombre, numero_control):
        self.nombre = nombre
        self.numero_control = numero_control
        self.libros_prestados = []  # Lista de libros que tiene prestados

    def tomar_prestado(self, libro):
        # Un alumno toma un libro si no está prestado
        if not libro.prestado:
            libro.marcar_prestado()
            self.libros_prestados.append(libro)
            print(f"{self.nombre} ha tomado prestado el libro: {libro.titulo}")
        else:
            print(f"El libro '{libro.titulo}' ya está prestado.")

    def devolver_libro(self, libro):
        # Un alumno devuelve un libro
        if libro in self.libros_prestados:
            libro.marcar_devuelto()
            self.libros_prestados.remove(libro)  # quitar libro de la lista
            print(f"{self.nombre} ha devuelto el libro: {libro.titulo}")
        else:
            print(f"{self.nombre} no tiene ese libro prestado.")


# Clase Biblioteca: administra libros y alumnos
class Biblioteca:
    def __init__(self):
        self.libros = []   # Lista de libros disponibles
        self.alumnos = []  # Lista de alumnos registrados

    def agregar_libro(self, libro):
        self.libros.append(libro)

    def registrar_alumno(self, alumno):
        self.alumnos.append(alumno)

    def mostrar_libros_disponibles(self):
        print(" Libros disponibles en la biblioteca:")
        for libro in self.libros:
            if not libro.prestado:
                libro.mostrar_info()

    def mostrar_prestamos_alumno(self, numero_control):
        # Buscar al alumno por su número de control
        for alumno in self.alumnos:
            if alumno.numero_control == numero_control:
                print(f"Préstamos de {alumno.nombre}:")
                if alumno.libros_prestados:
                    for libro in alumno.libros_prestados:
                        libro.mostrar_info()
                else:
                    print("No tiene libros prestados.")
                return
        print("Alumno no encontrado.")


# Crear la biblioteca
biblioteca = Biblioteca()

# Crear libros
libro1 = Libro("cisco lovers", "jesus ivan esquivel ruiz", 2025)
libro2 = Libro("guia para usar el laboratorio de redes", "el jerry", 1943)
libro3 = Libro("cisco CCNA", "netacad", 2023)

# Agregar libros a la biblioteca
biblioteca.agregar_libro(libro1)
biblioteca.agregar_libro(libro2)
biblioteca.agregar_libro(libro3)

# Crear alumnos
alumno1 = Alumno("Jesus Esquivel", "2403150038")
alumno2 = Alumno("Tania Esquivel", "2403150039")

# Registrar alumnos en la biblioteca
biblioteca.registrar_alumno(alumno1)
biblioteca.registrar_alumno(alumno2)

# Ana toma prestado un libro
alumno1.tomar_prestado(libro1)

# Mostrar libros disponibles después del préstamo
biblioteca.mostrar_libros_disponibles()

# Mostrar préstamos de un alumno
biblioteca.mostrar_prestamos_alumno("2403150038")

# Ana devuelve el libro
alumno1.devolver_libro(libro1)

# Mostrar libros disponibles después de la devolución
biblioteca.mostrar_libros_disponibles()
