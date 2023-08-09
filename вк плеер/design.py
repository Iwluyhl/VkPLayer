import customtkinter as ctk
import tkinter as tk


class MainUi:
    def __init__(self):
        self.app = ctk.CTk()
        self.app.geometry("600x500")
        self.app.resizable(False, False)
        self.btn_load = ctk.CTkButton(self.app, text="Загрузить треки")
        self.btn_load.pack()
        self.listbox = tk.Listbox(self.app, height=20, width=55, bg="#481254", fg="#D386E4")
        self.listbox.pack()
        self.app.withdraw()

    def run(self):
        self.app.mainloop()
