# Clase Libro: representa un libro con título, autor y año
class Libro:
    def __init__(self, titulo, autor, anio):
        # Atributos de la clase Libro
        self.titulo = titulo
        self.autor = autor
        self.anio = anio
        self.id = None   # El ID se asignará después en la Biblioteca

    def asignar_id(self, id_libro):
        # Método para asignar un ID único al libro
        self.id = id_libro

    def mostrar_info(self):
        # Muestra en pantalla la información del libro
        print(f"ID: {self.id} | Título: {self.titulo} | Autor: {self.autor} | Año: {self.anio}")


# Clase Biblioteca: contiene una lista de libros y métodos para gestionarlos
class Biblioteca:
    def __init__(self):
        # Lista vacía donde se guardarán los objetos Libro
        self.libros = []
        # Contador de IDs para cada libro
        self.contador_id = 1

    def agregar_libro(self, titulo, autor, anio):
        # Crear un nuevo objeto de tipo Libro
        nuevo_libro = Libro(titulo, autor, anio)
        # Asignar ID usando el contador
        nuevo_libro.asignar_id(self.contador_id)
        # Agregar el libro a la lista
        self.libros.append(nuevo_libro)
        # Aumentar el contador para el siguiente libro
        self.contador_id += 1

    def mostrar_biblioteca(self):
        # Muestra la información de todos los libros guardados
        print(" ciu de la Unipolli ")
        for libro in self.libros:
            libro.mostrar_info()


# -------------------- EJEMPLO DE USO --------------------
# Crear una biblioteca
biblioteca = Biblioteca()

# Agregar libros
biblioteca.agregar_libro("el arqui", "juve 3 d estudio", 2024)
biblioteca.agregar_libro("baldor", "matematico baldor", 1949)
biblioteca.agregar_libro("cisco", "netacad", 2025)

# Mostrar toda la biblioteca
biblioteca.mostrar_biblioteca()

# Ejemplo de acceso a un libro en específico (nivel de abstracción)
biblioteca.libros[0].mostrar_info()
