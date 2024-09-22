import tkinter as tk
from tkinter import messagebox

# Clase base
class MainWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Ventana Principal")
        self.root.geometry("400x300")
        self.root.resizable(False, False)
        self.root.config(bg="#7FFFD4")
        self.root.protocol("WM_DELETE_WINDOW", self.on_close)

    def on_close(self):
        # Mostrar ventana emergente de advertencia
        if messagebox.askokcancel("Cerrar", "¿Estás seguro de que quieres cerrar la ventana?"):
            self.root.destroy()

# Subclase
class CustomWindow(MainWindow):
    def __init__(self, root):
        super().__init__(root)

    def on_close(self):
        if messagebox.askyesno("Confirmar Cierre", "¿Realmente quieres salir?"):
            self.root.destroy()


root = tk.Tk()
custom_window = CustomWindow(root)
root.mainloop()
