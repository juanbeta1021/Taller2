import tkinter as tk
from tkinter import messagebox

class InfoPopup:
    def __init__(self, info_message):
        self.info_message = info_message

    def show_info(self):
        messagebox.showinfo("Información", self.info_message)

class ErrorPopup:
    def __init__(self, error_message):
        self.error_message = error_message

    def show_error(self):
        messagebox.showerror("Error", self.error_message)

class CustomPopup(InfoPopup, ErrorPopup):
    def __init__(self, info_message, error_message):
        InfoPopup.__init__(self, info_message)
        ErrorPopup.__init__(self, error_message)

    def show_custom_info(self):
        messagebox.showinfo("Información Personalizada", f"Mensaje informativo: {self.info_message}")

    def show_custom_error(self):
        messagebox.showerror("Error Personalizado", f"¡Error encontrado! Detalles: {self.error_message}")

    def show_both(self):
        self.show_custom_info()
        self.show_custom_error()

root = tk.Tk()
root.withdraw()
custom_popup = CustomPopup("Este es un mensaje de información.", "Este es un mensaje de error.")
custom_popup.show_both()
root.mainloop()
