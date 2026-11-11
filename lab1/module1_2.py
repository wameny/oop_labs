#варіант 2

import tkinter as tk

class Window2:
    def __init__(self, parent, on_back):
        self.parent = parent
        self.on_back = on_back
        self.window = tk.Toplevel(parent)
        self.window.title('Робота 1 - Вікно 2')
        self.window.geometry('700x500')
        self.window.grab_set()
    
        self.label = self._create_label('Second window')
    
        self._create_button('< Назад', self._go_previous)
        self._create_button('Так', self._yes_clicked)
        self._create_button('Відміна', self.window.destroy)
    
    def _go_previous(self):
        self.window.destroy()
        self.on_back()

    def _yes_clicked(self):
        self.label.config(text='Yes clicked')
    
    def _create_label(self, title):
        label = tk.Label(self.window, text=title, font=("Arial", 12))
        label.pack(pady=60)
    
        return label
        
    def _create_button(self, title, func):
        button = tk.Button(self.window, text=title, width=15, command=func)
        button.pack(pady=20)
    
        return button