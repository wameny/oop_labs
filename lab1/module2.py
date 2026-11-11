#варіант 3

import tkinter as tk

class Work2:
    def __init__(self, parent, callback_func):
        self.window = tk.Toplevel(parent)
        self.window.title('Робота 2')
        self.window.geometry('700x500')
        self.window.grab_set()
        self.callback_func = callback_func

        self._create_items()

    def _create_items(self):
        self._create_label('Виберіть вашу групу:')

        self.listbox = tk.Listbox(self.window, font=("Arial", 11), height=6, selectmode=tk.SINGLE)
        self.listbox.pack(pady=10, padx=20, fill="both", expand=True)

        groups = ["ІМ-51", "ІМ-52", "ІМ-53", "ІМ-54", "ІМ-55", "ІМ-о51"]
        for group in groups:
            self.listbox.insert(tk.END, group)

        self._create_button('Так', self._on_yes_clicked)

    def _on_yes_clicked(self):
        selected_indices = self.listbox.curselection()
        if selected_indices:
            index = selected_indices[0]
            group_name = self.listbox.get(index)
            
            if self.callback_func:
                self.callback_func(group_name)
                
        self.window.destroy()

    def _create_label(self, title):
        label = tk.Label(self.window, text=title, font=("Arial", 12))
        label.pack(pady=60)
        
        return label
            
    def _create_button(self, title, func):
        button = tk.Button(self.window, text=title, width=15, command=func)
        button.pack(pady=20)
        
        return button