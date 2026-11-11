#варіант 2

import tkinter as tk

class Window1:
    def __init__(self, parent, on_next):
        self.parent = parent
        self.on_next = on_next
        self.window = tk.Toplevel(parent)
        self.window.title('Робота 1 - Вікно 1')
        self.window.geometry('700x500')
        self.window.grab_set()

        self._create_label('First window')

        self._create_button('Далі >', self._go_next)

        self._create_button('Відміна', self.window.destroy)

    def _go_next(self):
        self.window.destroy()
        self.on_next()

    def _create_label(self, title):
        label = tk.Label(self.window, text=title, font=("Arial", 12))
        label.pack(pady=60)

        return label
    
    def _create_button(self, title, func):
        button = tk.Button(self.window, text=title, width=15, command=func)
        button.pack(pady=20)

        return button