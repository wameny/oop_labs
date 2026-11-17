import tkinter as tk
from tkinter import messagebox
from shape_editor import ShapeObjectsEditor

class Main:
    def __init__(self, root):
        self.root = root
        self.root.title('Graphic editor')
        self.root.geometry('1000x600')

        self.canvas = tk.Canvas(root, width=800, height=600, bg="white")
        self.canvas.pack(fill=tk.BOTH, expand=True)

        self.editor = ShapeObjectsEditor(self.canvas)

        self.canvas.bind("<Button-1>", self.editor.on_lb_down)
        self.canvas.bind("<B1-Motion>", self.editor.on_mouse_move)
        self.canvas.bind("<ButtonRelease-1>", self.editor.on_lb_up)

        self.mode = tk.StringVar(value="")

        menu = tk.Menu(root)
        root.config(menu=menu)

        file_menu = tk.Menu(menu, tearoff=0)
        file_menu.add_command(label="Вихід", command=root.destroy)
        menu.add_cascade(label="Файл", menu=file_menu)

        object_menu = tk.Menu(menu, tearoff=0)
        object_menu.add_radiobutton(label='Крапка', command=self.editor.start_point_editor)
        object_menu.add_radiobutton(label='Лінія', command=self.editor.start_line_editor)
        object_menu.add_radiobutton(label='Прямокутник', command=self.editor.start_rectangle_editor)
        object_menu.add_radiobutton(label='Еліпс', command=self.editor.start_ellipse_editor)
        menu.add_cascade(label='Об`єкти', menu=object_menu)

        info_menu = tk.Menu(menu, tearoff=0)
        info_menu.add_command(label='Про програму', command=lambda: messagebox.showinfo("Про програму", "Лабораторна робота 2"))
        menu.add_cascade(label='Довідка', menu=info_menu)

if __name__ == '__main__':
    root = tk.Tk()
    main = Main(root)
    root.mainloop()