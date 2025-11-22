import tkinter as tk
from tkinter import ttk, messagebox, Label, PhotoImage
from modelos import Biblioteca, Libro, Usuario


class BibliotecaApp:
    def __init__(self, root):
        self.biblioteca = Biblioteca()
        self.root = root
        self.root.title("📚 Biblioteca - Sistema de Gestión")
        self.root.geometry("600x750")
        self.root.config(bg= "#C84444")

        # ==========================================================
        # ESTILOS MODERNOS
        # ==========================================================
        style = ttk.Style()
        style.theme_use("clam")


        style.configure(
            "Modern.TButton",
            font=("Arial", 12, "bold"),
            padding=10,
            foreground="#FFFFFF",
            background="#5A1E1E",
            borderwidth=0,
            focusthickness=3,
            focuscolor="none",
        )
        style.map(
        "Modern.TButton",
        background=[("active", "#7A2A2A")]
        )
        style.configure("Modern.TLabelframe", background="#F8D9D9")
        style.configure("Modern.TLabelframe.Label", font=("Arial", 12, "bold"), background="#F8D9D9")
        style.configure("Modern.TLabel", background="#F8D9D9", font=("Arial", 11))

        # ==========================================================
        # Título principal
        # ==========================================================
        tk.Label(root, text="Sistema de Biblioteca", font=("Arial", 30, "bold"), bg="#C84444", fg="white").pack(pady=10)

        # ==========================================================FS
        # Sección: Registro de usuarios
        # ==========================================================
        frame_usuario = tk.LabelFrame(root, text="Registro de usuario", padx=10, pady=10)
        frame_usuario.pack(fill="x", padx=10, pady=5)

        tk.Label(frame_usuario, text="Nombre:", bg= "#f7d3d3", font=("Arial", 12)).grid(row=0, column=0)
        self.nombre_usuario = tk.Entry(frame_usuario, width=20)      
        self.nombre_usuario.grid(row=0, column=1, padx=10)

        tk.Label(frame_usuario, text="ID:", bg= "#f7d3d3", font=("Arial", 12)).grid(row=0, column=2)
        validar_cmd = (self.root.register(self.validar_id), "%P")
        self.id_usuario = tk.Entry(frame_usuario, width=10, validate="key", validatecommand=validar_cmd)
        self.id_usuario.grid(row=0, column=3, padx=5)

        ttk.Button(frame_usuario, text="Registrar", style="Modern.TButton", command=self.registrar_usuario).grid(row=0, column=5, padx=5)


        tk.Label(frame_usuario, text="Usuario activo:",bg= "#f7d3d3", font=("Arial", 12)).grid(row=1, column=0, pady=10)
        self.combo_usuarios = ttk.Combobox(frame_usuario, state="readonly", width=20)
        self.combo_usuarios.grid(row=1, column=1, columnspan=3, pady=10, sticky="w")
        
        ttk.Button(frame_usuario, text="Ver prestados", style="Modern.TButton", command=self.Actualizar_prestados_usuario).grid(row=3, column=1, padx=5)

        # ==========================================================
        # Sección: Agregar libros
        # ==========================================================
        frame_libro = tk.LabelFrame(root, text="Agregar libro", padx=10, pady=10)
        frame_libro.pack(fill="x", padx=10, pady=5)

        tk.Label(frame_libro, text="Título:",bg= "#f7d3d3", font=("Arial", 12)).grid(row=0, column=0)
        self.titulo_entry = tk.Entry(frame_libro, width=30)
        self.titulo_entry.grid(row=0, column=1, padx=5)

        tk.Label(frame_libro, text="Autor:", bg= "#f7d3d3", font=("Arial", 12)).grid(row=1, column=0)
        self.autor_entry = tk.Entry(frame_libro, width=30)
        self.autor_entry.grid(row=1, column=1, padx=5)

        ttk.Button(frame_libro, text="Agregar", style="Modern.TButton", command=self.agregar_libro).grid(row=2, column=0, columnspan=2, pady=5)


        # ==========================================================
        # Sección: Lista de libros
        # ==========================================================
        frame_lista = tk.LabelFrame(root, text="Libros disponibles", padx=10, pady=10)
        frame_lista.pack(fill="both", expand=True, padx=10, pady=5)

        self.lista_libros = tk.Listbox(frame_lista, height=5)
        self.lista_libros.pack(fill="both", expand=True)

        # ==========================================================
        # Sección: Lista de libros prestados
        # ==========================================================
        frame_prestados = tk.LabelFrame(root, text="Libros prestados por el usuario seleccionado", padx=10, pady=10)
        frame_prestados.pack(fill="both", expand=True, padx=10, pady=5)

        self.lista_prestados = tk.Listbox(frame_prestados, height=5)
        self.lista_prestados.pack(fill="both", expand=True)

        # ==========================================================
        # Botones de acción
        # ==========================================================
        frame_botones = tk.Frame(root)
        frame_botones.pack(pady=10)

        ttk.Button(frame_botones, text=" + Prestar libro", style="Modern.TButton", command=self.prestar_libro).grid(row=0, column=0, padx=5)

        ttk.Button(frame_botones, text=" - Devolver libro", style="Modern.TButton", command=self.devolver_libro).grid(row=0, column=1, padx=5)
        self.actualizar_lista()

    	# ==========================================================
        # Datos hardcodeados
        # ==========================================================
        # Usuarios iniciales
        u1 = Usuario("Juan Perez", "101")
        u2 = Usuario("Ana Gomez", "102")
        u3 = Usuario("Carlos Ruiz", "103")

        self.biblioteca.registrar_usuario(u1)
        self.biblioteca.registrar_usuario(u2)
        self.biblioteca.registrar_usuario(u3)

        # Libros iniciales
        l1 = Libro("El Principito", "Antoine de Saint-Exupéry")
        l2 = Libro("1984", "George Orwell")
        l3 = Libro("Cien Años de Soledad", "Gabriel García Márquez")
        l4  = Libro("Don Quijote de la Mancha", "Miguel de Cervantes")
        l5  = Libro("La Sombra del Viento", "Carlos Ruiz Zafón")
        l6  = Libro("Fahrenheit 451", "Ray Bradbury")
        l7  = Libro("Orgullo y Prejuicio", "Jane Austen")
        l8  = Libro("Crimen y Castigo", "Fiódor Dostoyevski")
        l9  = Libro("El Hobbit", "J. R. R. Tolkien")
        l10 = Libro("El Alquimista", "Paulo Coelho")
        l11 = Libro("Matar a un Ruiseñor", "Harper Lee")
        l12 = Libro("El Señor de las Moscas", "William Golding")
        l13 = Libro("Drácula", "Bram Stoker")
        l14 = Libro("Frankenstein", "Mary Shelley")
        l15 = Libro("El Gran Gatsby", "F. Scott Fitzgerald")
        l16 = Libro("La Metamorfosis", "Franz Kafka")
        l17 = Libro("Los Juegos del Hambre", "Suzanne Collins")
        l18 = Libro("El Código Da Vinci", "Dan Brown")
        l19 = Libro("It", "Stephen King")
        l20 = Libro("El Viejo y el Mar", "Ernest Hemingway")

        self.biblioteca.agregar_libro(l1)
        self.biblioteca.agregar_libro(l2)
        self.biblioteca.agregar_libro(l3)
        self.biblioteca.agregar_libro(l4)
        self.biblioteca.agregar_libro(l5)
        self.biblioteca.agregar_libro(l6)
        self.biblioteca.agregar_libro(l7)
        self.biblioteca.agregar_libro(l8)
        self.biblioteca.agregar_libro(l9)
        self.biblioteca.agregar_libro(l10)
        self.biblioteca.agregar_libro(l11)
        self.biblioteca.agregar_libro(l12)
        self.biblioteca.agregar_libro(l13)
        self.biblioteca.agregar_libro(l14)
        self.biblioteca.agregar_libro(l15)
        self.biblioteca.agregar_libro(l16)
        self.biblioteca.agregar_libro(l17)
        self.biblioteca.agregar_libro(l18)  
        self.biblioteca.agregar_libro(l19)
        self.biblioteca.agregar_libro(l20)
        
        # Actualizamos listas en la interfaz
        self.actualizar_usuarios()
        self.actualizar_lista()    

        
    # ==========================================================
    # FUNCIONES DE INTERFAZ
    # ==========================================================
    def Actualizar_prestados_usuario(self):
            self.actualizar_prestados()
        
    def registrar_usuario(self):
        nombre = self.nombre_usuario.get().strip()
        usuario_id = self.id_usuario.get().strip()
        if not nombre or not usuario_id:
            messagebox.showwarning("Campos vacíos", "Debe ingresar nombre e ID del usuario.")
            return
        nuevo_usuario = Usuario(nombre, usuario_id)
        self.biblioteca.registrar_usuario(nuevo_usuario)
        self.actualizar_usuarios()
        self.nombre_usuario.delete(0, tk.END)
        self.id_usuario.delete(0, tk.END)
        messagebox.showinfo("Registro exitoso", f"Usuario '{nombre}' registrado correctamente.")

    def actualizar_usuarios(self):
        self.combo_usuarios["values"] = [u.nombre for u in self.biblioteca.usuarios]
        if not self.combo_usuarios.get() and self.biblioteca.usuarios:
            self.combo_usuarios.current(0)
        self.actualizar_prestados()

    def agregar_libro(self):
        titulo = self.titulo_entry.get().strip()
        autor = self.autor_entry.get().strip()
        if titulo and autor:
            nuevo_libro = Libro(titulo, autor)
            self.biblioteca.agregar_libro(nuevo_libro)
            self.actualizar_lista()
            self.titulo_entry.delete(0, tk.END)
            self.autor_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Campos vacíos", "Debe ingresar título y autor.")

    def actualizar_lista(self):
        self.lista_libros.delete(0, tk.END)
        for libro in self.biblioteca.libros:
            estado = "Disponible" if libro.disponible else "Prestado"
            self.lista_libros.insert(tk.END, f"{libro.titulo} - {libro.autor} [{estado}]")

    def actualizar_prestados(self):
        usuario = self.usuario_actual()
        self.lista_prestados.delete(0, tk.END)
        if usuario:
            for libro in usuario.libros_prestados:
                self.lista_prestados.insert(tk.END, f"{libro.titulo} - {libro.autor}")
            if not usuario.libros_prestados:
                self.lista_prestados.insert(tk.END, "No hay libros prestados.")
         
            

    def usuario_actual(self):
        nombre = self.combo_usuarios.get()
        for u in self.biblioteca.usuarios:
            if u.nombre == nombre:
                return u   
        return None
        

    def prestar_libro(self):
        usuario = self.usuario_actual()
        if not usuario:
            messagebox.showwarning("Sin usuario", "Debe seleccionar un usuario antes de prestar.")
            return
        seleccion = self.lista_libros.curselection()
        if not seleccion:
            messagebox.showinfo("Aviso", "Seleccione un libro.")
            return
        libro = self.biblioteca.libros[seleccion[0]]
        msg = usuario.prestar_libro(libro)
        messagebox.showinfo("Resultado", msg)
        self.actualizar_lista()
        self.actualizar_prestados()

    def devolver_libro(self):
        usuario = self.usuario_actual()
        if not usuario:
            messagebox.showwarning("Sin usuario", "Debe seleccionar un usuario antes de devolver.")
            return
        seleccion = self.lista_libros.curselection()
        if not seleccion:
            messagebox.showinfo("Aviso", "Seleccione un libro.")
            return
        libro = self.biblioteca.libros[seleccion[0]]
        msg = usuario.devolver_libro(libro)
        messagebox.showinfo("Resultado", msg)
        self.actualizar_lista()
        self.actualizar_prestados()
    def validar_id(self, texto):
        if texto.isdigit() or texto == "":
            return True
        else:
            messagebox.showwarning("ID inválido", "Solo se permiten números en el ID de usuario.")
        return False
    
# ==========================================================fin del archivo================================================ #