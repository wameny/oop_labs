#варіант 2

import tkinter as tk

class Work1:
    def __init__(self, parent):
        self.parent = parent
        self.open_window1()

    def open_window1(self):
        self.window1 = tk.Toplevel(self.parent)
        self.window1.title('Робота 1')
        self.window1.geometry('700x500')
        self.window1.grab_set()

        self.create_label('First page', self.window1)
        
        self.create_button('Далі >', self.go_to_window2, self.window1)
        self.create_button('Відміна', self.window1.destroy, self.window1)

    def open_window2(self):
        self.window2 = tk.Toplevel(self.parent)
        self.window2.title('Робота 2')
        self.window2.geometry('700x500')
        self.window2.grab_set()
        
        self.create_label('Second page', self.window2)
                
        self.create_button('< Назад', self.go_to_window1, self.window2)
        self.create_button('Так',  lambda: self.yes_clicked(self.window2), self.window2)
        self.create_button('Відміна', self.window2.destroy, self.window2)

    def go_to_window1(self):
        self.window2.destroy()
        self.open_window1()

    def go_to_window2(self):
        self.window1.destroy()
        self.open_window2()

    def yes_clicked(self, window):
        self.create_label('Yes clicked', window)

    def create_label(self, title, window):
        label = tk.Label(window, text=title, font=("Arial", 12))
        label.pack(pady=60)

        return label
    
    def create_button(self, title, func, window):
        button = tk.Button(window, text=title, width=15, command=func)
        button.pack(pady=20)

        return button