from abc import ABC, abstractmethod

class Shape(ABC):
    def __init__(self):
        self._x1 = 0
        self._y1 = 0
        self._x2 = 0
        self._y2 = 0

    def set(self, x1, y1, x2, y2):
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2

    @abstractmethod
    def show(self, canvas):
        pass

class PointShape(Shape):
    def __init__(self):
        super().__init__()

    def show(self, canvas):
        canvas.create_oval(self._x1, self._y1, self._x1 + 2, self._y1 + 2, fill="black")

class LineShape(Shape):
    def __init__(self):
            super().__init__()
    
    def show(self, canvas):
        canvas.create_line(self._x1, self._y1, self._x2, self._y2, fill="black")

class RectangleShape(Shape):
    def __init__(self):
        super().__init__()

    def show(self, canvas):
        canvas.create_rectangle(self._x1, self._y1, self._x2, self._y2, outline="black", fill='#00ffff')

class EllipseShape(Shape):
    def __init__(self):
        super().__init__()

    def show(self, canvas):
        canvas.create_oval(self._x1, self._y1, self._x2, self._y2, outline="black", fill="white")