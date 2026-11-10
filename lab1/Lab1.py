import tkinter as tk
import module1
import module2

class Main:
    def __init__(self, root):
        self.root = root
        self.root.title('Lab1')
        self.root.geometry('700x500')

        self.info_label = tk.Label(self.root, text="Waiting for text", font=("Arial", 12))
        self.info_label.pack(pady=60)

        self.create_menu()

    def create_menu(self):
        menu = tk.Menu(self.root)
        self.root.config(menu=menu)

        cascade_menu = tk.Menu(self.root, tearoff=0)
        menu.add_cascade(menu=cascade_menu)

        cascade_menu.add_command(label='Variant 2', command=self.var2_run)
        cascade_menu.add_command(label='Variant 3', command=self.var3_run)

    def var2_run(self):
        self.info_label.config(text='Variant 2 run')

    def var3_run(self):
        self.info_label.config(text='Variant 3 run')



if __name__ == '__main__':
    root = tk.Tk()
    main = Main(root)
    root.mainloop()