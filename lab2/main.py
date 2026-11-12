import tkinter as tk

class Main:
    def __init__(self, root):
        self.root = root
        self.root.title('Graphic editor')
        self.root.geometry('1000x600')

        canvas = tk.Canvas(root, width=800, height=600, bg="white")
        canvas.pack(fill=tk.BOTH, expand=True)

if __name__ == '__main__':
    root = tk.Tk()
    main = Main(root)
    root.mainloop()