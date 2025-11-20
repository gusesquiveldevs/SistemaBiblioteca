# ==========================================================
# CLASES DEL SISTEMA
# ==========================================================

class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.disponible = True

    def prestar(self):
        """Marca el libro como no disponible."""
        if self.disponible:
            self.disponible = False
            return f"✅ El libro '{self.titulo}' ha sido prestado."
        else:
            return f"❌ El libro '{self.titulo}' no está disponible."

    def devolver(self):
        """Marca el libro como disponible nuevamente."""
        if not self.disponible:
            self.disponible = True
            return f"📘 El libro '{self.titulo}' ha sido devuelto."
        else:
            return f"⚠️ El libro '{self.titulo}' ya estaba disponible."


class Usuario:
    def __init__(self, nombre, usuario_id):
        self.nombre = nombre
        self.usuario_id = usuario_id
        self.libros_prestados = []

    def prestar_libro(self, libro):
        """Permite al usuario tomar prestado un libro."""
        if libro.disponible:
            libro.disponible = False
            self.libros_prestados.append(libro)
            return f"✅ {self.nombre} ha prestado el libro '{libro.titulo}'."
        else:
            return f"❌ El libro '{libro.titulo}' no está disponible."

    def devolver_libro(self, libro):
        """Permite al usuario devolver un libro prestado."""
        if libro in self.libros_prestados:
            libro.disponible = True
            self.libros_prestados.remove(libro)
            return f"📗 {self.nombre} ha devuelto el libro '{libro.titulo}'."
        else:
            return f"⚠️ {self.nombre} no tiene el libro '{libro.titulo}' prestado."

    def to_dict(self):
        return {
            "nombre": self.nombre,
            "id_usuario": self.id_usuario,
            "libros_prestados": [libro.titulo for libro in self.libros_prestados]
        }

class Biblioteca:
    def __init__(self):
         self.libros = []
         self.usuarios = []

    def agregar_libro(self, libro):
        self.libros.append(libro)

    def registrar_usuario(self, usuario):
         self.usuarios.append(usuario)
