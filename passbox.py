import pickle
import random
import sys
import os
import customtkinter
from time import sleep
from helptext import Helptext
from enigma import Enigma

DEV = False  # if True imports ico in DEV mode

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

class App(customtkinter.CTk):
    def __init__(self, dev=False):
        super().__init__()

        self.DEV = dev
        self.END = 'end'
        self.NORMAL = 'normal'
        self.DISABLED = 'disabled'
        self.DICT = {}
        self.C_DICT = {}
        self.binfile = 'passbox.bin'
        self.icofile = 'passbox.ico'

        self.title("Passbox - Keeps your login/pass encrypted and safe")
        self.resizable(False, False)
        self.geometry('+70+70') # 'width x height + left + top'
        self.protocol("WM_DELETE_WINDOW", self.on_closing)  # call .on_closing() when app gets closed

        self.font = customtkinter.CTkFont(family='Verdana', size=14)

        # ============ create two frames ============
        # configure grid layout (2x1)

        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.frame_left = customtkinter.CTkFrame(master=self,
                                                 corner_radius=3)
        self.frame_left.grid(row=0, column=0, sticky="nswe", padx=10, pady=10)

        self.frame_right = customtkinter.CTkFrame(master=self,
                                                  corner_radius=3)
        self.frame_right.grid(row=0, column=1, sticky="nswe", padx=10, pady=10)

        # ============ frame_left ============

        self.label_left = customtkinter.CTkLabel(master=self.frame_left,
                                              text="app : [login] [pass]",
                                              font=self.font)
        self.label_left.grid(row=1, column=0, pady=5, padx=10, sticky="w")
        
        self.text = customtkinter.CTkTextbox(master=self.frame_left,
                                             width=600,
                                             height=400,
                                             font=self.font)
        self.text.grid(row=2, column=0, pady=10, padx=10)

        self.text.insert('1.0', random.choice(Helptext.hello))

        # ============ frame_right ============ column0

        self.label_right1 = customtkinter.CTkLabel(master=self.frame_right, text="app:")
        self.label_right1.grid(row=4, column=0, pady=0, padx=10, sticky="w")

        self.label_right2 = customtkinter.CTkLabel(master=self.frame_right, text="login:")
        self.label_right2.grid(row=5, column=0, pady=0, padx=10, sticky="w")

        self.label_right3 = customtkinter.CTkLabel(master=self.frame_right, text="pass:")
        self.label_right3.grid(row=6, column=0, pady=0, padx=10, sticky="w")

        # ============ frame_right ============ column1

        self.frame_right.grid_rowconfigure(9, weight=1)  # empty row as spacing
        self.frame_right.grid_rowconfigure(11, minsize=5)  # empty row as spacing
        #0
        self.key_chbox_var = customtkinter.IntVar(value=1)
        self.key_chbox = customtkinter.CTkCheckBox(master=self.frame_right,
                                                 text='hide key',
                                                 variable=self.key_chbox_var,
                                                 command=self.hide_key)
        self.key_chbox.grid(row=0, column=1, pady=10, padx=10)
        #1
        self.key_entry_var = customtkinter.StringVar()
        self.key_entry = customtkinter.CTkEntry(master=self.frame_right,
                                                textvariable=self.key_entry_var)
        self.key_entry.grid(row=1, column=1, pady=5, padx=10)
        #2
        self.load_btn = customtkinter.CTkButton(master=self.frame_right,
                                                text='show',
                                                command=self.show_dict)
        self.load_btn.grid(row=2, column=1, pady=5, padx=10)
        #3
        self.add_btn = customtkinter.CTkButton(master=self.frame_right,
                                               text='add',
                                               command=self.add)
        self.add_btn.grid(row=3, column=1, pady=5, padx=10)
        #4
        self.app_entry_var = customtkinter.StringVar()
        self.app_entry = customtkinter.CTkEntry(master=self.frame_right,
                                                textvariable=self.app_entry_var)
        self.app_entry.grid(row=4, column=1, pady=5, padx=10, columnspan=2, sticky="nsew")
        #5
        self.login_entry_var = customtkinter.StringVar()
        self.login_entry = customtkinter.CTkEntry(master=self.frame_right,
                                                  textvariable=self.login_entry_var)
        self.login_entry.grid(row=5, column=1, pady=5, padx=10, columnspan=2, sticky="nsew")
        #6
        self.pass_entry_var = customtkinter.StringVar()
        self.pass_entry = customtkinter.CTkEntry(master=self.frame_right,
                                                 textvariable=self.pass_entry_var)
        self.pass_entry.grid(row=6, column=1, pady=5, padx=10, columnspan=2, sticky="nsew")
        #10
        self.optionmenu = customtkinter.CTkOptionMenu(master=self.frame_right,
                                                        values=["Light", "Dark", "System"],
                                                        command=self.change_appearance_mode)
        self.optionmenu.grid(row=10, column=1, pady=5, padx=10)

        # ============ frame_right ============ column2
        #0
        self.pin_chbox_var = customtkinter.IntVar(value=1)
        self.pin_chbox = customtkinter.CTkCheckBox(master=self.frame_right,
                                                 text='hide pin',
                                                 variable=self.pin_chbox_var,
                                                 command=self.hide_pin)
        self.pin_chbox.grid(row=0, column=2, pady=5)
        #1
        self.pin_entry_var = customtkinter.StringVar()
        self.pin_entry = customtkinter.CTkEntry(master=self.frame_right,
                                                textvariable=self.pin_entry_var)
        self.pin_entry.grid(row=1, column=2, pady=5, padx=10)
        #2
        self.new_btn = customtkinter.CTkButton(master=self.frame_right,
                                                text='new',
                                                command=self.new_button)
        self.new_btn.grid(row=2, column=2, pady=5, padx=10)
        #3
        self.del_btn = customtkinter.CTkButton(master=self.frame_right,
                                               text='del',
                                               command=self.delete)
        self.del_btn.grid(row=3, column=2, pady=5, padx=10)
        #10
        self.help_btn = customtkinter.CTkButton(master=self.frame_right,
                                                width=3,
                                                text='?',
                                                command=lambda: self.text_print(Helptext.help_text))
        self.help_btn.grid(row=10, column=2, pady=5, padx=10)
        
        # default
        self.get_ico()
        self.optionmenu.set("System")
        self.key_entry.configure(show='*')
        self.pin_entry.configure(show='*')
        self.new_btn.configure(state=self.DISABLED)

    def change_appearance_mode(self, new_appearance_mode):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def on_closing(self, event=0):
        self.destroy()

    def get_ico(self):
        try:
            if self.DEV:
                self.iconbitmap(default=self.icofile)
                return
            path = os.path.join(sys._MEIPASS, self.icofile)
            self.iconbitmap(default=path)
        except:
            pass

    def hide_key(self):
        "hide kye changing key_entry param"
        if self.key_chbox_var.get():
            self.key_entry.configure(show='*')
        else:
            self.key_entry.configure(show='')

    def hide_pin(self):
        "hide pin changing pin_entry param"
        if self.pin_chbox_var.get():
            self.pin_entry.configure(show='*')
        else:
            self.pin_entry.configure(show='')

    def interface_disable(self):
        self.new_btn.configure(state=self.NORMAL)
        self.load_btn.configure(state=self.DISABLED)
        self.app_entry.configure(state=self.DISABLED)
        self.login_entry.configure(state=self.DISABLED)
        self.pass_entry.configure(state=self.DISABLED)
        self.add_btn.configure(state=self.DISABLED)
        self.del_btn.configure(state=self.DISABLED)

    def interface_enable(self):
        self.new_btn.configure(state=self.DISABLED)
        self.load_btn.configure(state=self.NORMAL)
        self.app_entry.configure(state=self.NORMAL)
        self.login_entry.configure(state=self.NORMAL)
        self.pass_entry.configure(state=self.NORMAL)
        self.add_btn.configure(state=self.NORMAL)
        self.del_btn.configure(state=self.NORMAL)

    def new_button(self):
        sleep(0.3)
        "creates dict with CONTROL value"
        pin = self.pin_entry.get()
        if pin.isdigit() and len(pin) == 4:
            CONTROL = Enigma.control(pin)
            self.DICT = {CONTROL: ['', ''], 'passbox': ['pin', pin]}
            self.save_dict()
            self.interface_enable()
            self.text_print(Helptext.help_text_2)
        else:
            self.text_print("Pin doesn't match!\nEnter 4 digits! (example: 1234)")

    def show_dict(self):
        "shows dict in Textbox"
        sleep(0.3)
        self.load_dict()
        text_string = ''
        for i, j in sorted(self.DICT.items()):
            if j[0] != '' and j[1] != '':
                text_string += f'{i} : [{j[0]}] [{j[1]}]\n'
        self.text_print(text_string)

    def add(self):
        "add entry to dict"
        sleep(0.3)
        CONTROL = Enigma.control(self.pin_entry.get())
        if CONTROL in self.DICT:
            self.DICT[self.app_entry.get()] = [self.login_entry.get(), 
                                               self.pass_entry.get()]
            self.clear()
            self.save_dict()
            self.show_dict()
        else:
            self.text_print("Bad key or pin")

    def delete(self):
        "del entry from dict"
        sleep(0.3)
        CONTROL = Enigma.control(self.pin_entry.get())
        if CONTROL in self.DICT:
            self.DICT.pop(self.app_entry.get(), None)
            self.clear()
            self.save_dict()
            self.show_dict()
        else:
            self.text_print("Bad key or pin")

    def clear(self):
        self.app_entry.delete(0, self.END)
        self.login_entry.delete(0, self.END)
        self.pass_entry.delete(0, self.END)

    def load_dict(self):
        "load and encrypt dict"
        try:
            with open(self.binfile, 'rb') as f:
                self.C_DICT = pickle.load(f)
            self.DICT = self.crypt_dict(self.C_DICT)
            # print('C_DICT', self.C_DICT, '\nDICT', self.DICT)  #test
        except FileNotFoundError:
            self.interface_disable()
            self.text_print(Helptext.help_text_1)

    def save_dict(self):
        "crypt and save dict"
        self.C_DICT = self.crypt_dict(self.DICT)
        try:
            with open(self.binfile, 'wb') as f:
                pickle.dump(self.C_DICT, f)
        except PermissionError:
            self.text_print(f"Permission Error\nCannot save {self.binfile} file")

    def crypt_dict(self, indict: dict) -> dict:
        "crypt/encrypt dict"
        key = self.key_entry.get()
        outdict = {}
        for i, j in indict.items():
            outdict[Enigma.crypt_word(i, key)] = [Enigma.crypt_word(j[0], key), 
                                                  Enigma.crypt_word(j[1], key)]
        # Enigma.crypt_word(word:str, key:str)->str - crypt/encrypt word with key
        return outdict

    def text_print(self, text):
        "print tex to Textbox"
        self.text.delete('1.0', self.END)
        self.text.insert('1.0', text)


if __name__ == "__main__":
    app = App(dev=DEV)
    app.load_dict() # if dict not exists interface_disable()
    app.mainloop()

