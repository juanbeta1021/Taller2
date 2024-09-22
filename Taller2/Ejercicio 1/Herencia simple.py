import tkinter as tk
from tkinter import messagebox


# Clase base
class PopupBase:
    def __init__(self, message):
        self.message = message

    def show_message(self):
        messagebox.showinfo("Información", self.message)

# Clase hija
class CustomPopup(PopupBase):
    def __init__(self, message):
        super().__init__(message)

    def show_message(self):
        messagebox.showinfo("Ventana Personalizada", f"Mensaje personalizado: {self.message}")

root = tk.Tk()
root.withdraw()
popup = CustomPopup("Este es un mensaje desde la clase hija")
popup.show_message()
root.mainloop()
