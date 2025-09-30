# Clase Libro: representa un libro individual
class Libro:
    # Constructor: inicializa los atributos del objeto Libro
    def __init__(self, titulo, autor, año):
        self.titulo = titulo              # Guarda el título del libro
        self.autor = autor                # Guarda el autor del libro
        self.año = año                    # Guarda el año de publicación
        self.id = None                    # El ID aún no se asigna, por eso se pone None
        self.descripcion = ""             # Se inicializa como cadena vacía, sin descripción

    # Método para asignar un ID único al libro
    def asignar_id(self, id_libro):
        self.id = id_libro                # Asigna el ID recibido al atributo del libro

    # Método para asignar una descripción al libro
    def asignar_descripcion(self, descripcion):
        self.descripcion = descripcion    # Guarda la descripción en el atributo correspondiente

    # Método para mostrar toda la información del libro
    def mostrar_info(self):
        # Se usa f-string para imprimir los atributos del libro de forma clara
        print(f"ID: {self.id}")
        print(f"Título: {self.titulo}")
        # el f incerta vsalores en una cadena de texto 
        print(f"Autor: {self.autor}")
        print(f"Año: {self.año}")
        print(f"Descripción: {self.descripcion}")

# Clase Biblioteca: representa una colección de libros
class Biblioteca:
    # Constructor: inicializa la lista de libros
    def __init__(self):
        self.libros = []                  # Lista vacía donde se guardarán los libros

    # Método para agregar un nuevo libro a la biblioteca
    def agregar_libro(self, titulo, autor, año, descripcion):
        nuevo_libro = Libro(titulo, autor, año)  # Se crea un nuevo objeto Libro

        # Se asigna un ID autoincremental usando len() para contar los libros actuales
        # len(self.libros) cuenta cuántos libros hay en la lista
        # +1 asegura que el nuevo libro tenga un ID único y consecutivo
        nuevo_libro.asignar_id(len(self.libros) + 1)

        # Se asigna la descripción al libro
        nuevo_libro.asignar_descripcion(descripcion)

        # Se guarda el libro en la lista usando append()
        # append agrega el nuevo libro al final de la lista
        self.libros.append(nuevo_libro)

# Aquí se crea el objeto biblioteca usando la clase Biblioteca
# Se guarda en la variable 'biblioteca' para poder usar sus métodos
biblioteca = Biblioteca()

# Se agregan dos libros a la biblioteca usando el método agregar_libro()
biblioteca.agregar_libro("Redes y telecomunicaciones", "Jesús Iván Esquivel Ruiz", 2025, "Nuevo libro de la carrera")
biblioteca.agregar_libro("La Unipoli", "Jesús Esquivel", 2006, "Habla sobre la fabulosa carrera de redes y telecomunicaciones")

# Se accede al primer libro de la lista usando indexación [0]
# Los índices en Python empiezan desde 0, así que [0] es el primer libro
primer_libro = biblioteca.libros[0]

# Se llama al método mostrar_info() del primer libro
# Esto imprime todos sus datos en consola
primer_libro.mostrar_info()

                      



