import tkinter as tk
from tkinter import ttk, messagebox
from interfaz import BibliotecaApp
#from logicatxt import Biblioteca

if __name__ == "__main__":
    root = tk.Tk()
    app = BibliotecaApp(root)
    root.mainloop()