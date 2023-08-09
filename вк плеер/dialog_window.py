import tkinter as tk
import customtkinter as ctk
import vk_api


class Dialog:
    def __init__(self, program):
        self.window = tk.Tk()
        self.window.geometry("300x200")
        self.window.resizable(False, False)
        self.login = tk.Entry(self.window)
        self.login.pack()
        self.password = tk.Entry(self.window)
        self.password.pack()
        self.authButt = tk.Button(self.window, text="Авторизация", command=self.auth)
        self.authButt.pack()
        self.program = program
    
    def auth(self):
        login = self.login.get()
        password = self.password.get()
        
        print('успешная автоизация')
        
        self.api = vk_api.VkApi(login=login, password=password, auth_handler=self.two_factor,
                                captcha_handler=self.captcha)
        self.api.auth()
        
        self.program.app.deiconify()
        self.program.api = self.api
        self.window.destroy()
    
    def two_factor(self):
        remember_device = True
        self.dialog = ctk.CTkInputDialog(text="Введите код:", title="Test")
        code = self.dialog.get_input()
        print("Код:", code)
        return code, remember_device
    
    def captcha(self, captcha):
        captcha_code = input("Enter Captcha {0}: ".format(captcha.get_url())).strip()
        return captcha.try_again(captcha_code)