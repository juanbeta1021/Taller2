import tkinter as tk
from tkinter import messagebox

# Clase base
class ErrorPopup:
    def __init__(self, message):
        self.message = message

    def show_error(self):
        messagebox.showerror("Error", self.message)

# Clase hija
class CustomErrorPopup(ErrorPopup):
    def __init__(self, message):
        super().__init__(message)

    def show_error(self):
        messagebox.showerror("Error Personalizado", f"¡Ha ocurrido un error! Detalles: {self.message}")

root = tk.Tk()
root.withdraw()
custom_error_popup = CustomErrorPopup("Archivo no encontrado.")
custom_error_popup.show_error()
root.mainloop()
