#варіант 2

import tkinter as tk

class Work1:
    def __init__(self, parent):
        self.window = tk.Toplevel(parent)
        self.window.title('Робота 1')
        self.window.geometry('700x500')

        self.window.grab_set()

        self.label = tk.Label(self.window, font=("Arial", 12))
        self.label.pack(pady=60)

        self.show_step1()

    def clear_window(self):
        for widget in self.window.winfo_children():
            widget.destroy()

    def show_step1(self):
        self.clear_window()

        self.create_label('First page')

        self.create_button('Далі >', self.show_step2)
        self.create_button('Відміна', self.window.destroy)

    def show_step2(self):
        self.clear_window()

        self.create_label('Second page')

        self.create_button('< Назад', self.show_step1)
        self.create_button('Так', self.yes_clicked)
        self.create_button('Відміна', self.window.destroy)


    def yes_clicked(self):
        self.create_label('Yes clicked')

    def create_label(self, title):
        label = tk.Label(self.window, text=title, font=("Arial", 12))
        label.pack(pady=60)

        return label
    
    def create_button(self, title, func):
        button = tk.Button(self.window, text=title, width=15, command=func)
        button.pack(pady=20)

        return button