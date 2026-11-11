import tkinter as tk
import module1_1
import module1_2
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
        menu.add_cascade(menu=cascade_menu, label='Menu')

        cascade_menu.add_command(label='Робота 1', command=self.open_window1)
        cascade_menu.add_command(label='Робота 2', command=self.work2_run)

    def open_window1(self):
        module1_1.Window1(self.root, on_next=self.open_window2)

    def open_window2(self):
        module1_2.Window2(self.root, on_back=self.open_window1)
        
    def work2_run(self):
        module2.Work2(self.root, callback_func=self.receive_group_result)

    def receive_group_result(self, group_name):
        self.info_label.config(text=f"Вибрана група: {group_name}")



if __name__ == '__main__':
    root = tk.Tk()
    main = Main(root)
    root.mainloop()