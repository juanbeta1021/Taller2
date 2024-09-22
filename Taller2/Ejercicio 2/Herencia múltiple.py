import tkinter as tk
from tkinter import messagebox

class InfoPopup:
    def __init__(self, message):
        self.message = message

    def show_info(self):
        messagebox.showinfo("Información", self.message)

class WarningPopup:
    def __init__(self, message):
        self.message = message

    def show_warning(self):
        messagebox.showwarning("Advertencia", self.message)

class CombinedPopup(InfoPopup, WarningPopup):
    def __init__(self, info_message, warning_message):
        InfoPopup.__init__(self, info_message)   # Inicializar la parte de InfoPopup
        WarningPopup.__init__(self, warning_message)  # Inicializar la parte de WarningPopup

    def show_both(self):
        self.show_info()   # Mostrar el mensaje informativo
        self.show_warning()  # Mostrar el mensaje de advertencia

root = tk.Tk()
root.withdraw()
combined_popup = CombinedPopup("Este es un mensaje de información.", "Este es un mensaje de advertencia.")
combined_popup.show_both()
root.mainloop()
