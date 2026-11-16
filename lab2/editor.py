from abc import ABC, abstractmethod
from shape import PointShape, LineShape, RectangleShape, EllipseShape 

class Editor(ABC):
    @abstractmethod
    def on_lb_down(self, event):
        pass

    @abstractmethod
    def on_lb_up(self, event):
        pass

    @abstractmethod
    def on_mouse_move(self, event):
        pass

    @abstractmethod
    def on_paint(self):
        pass

class ShapeEditor(Editor):
    def __init__(self, owner, canvas):
        self._owner = owner
        self._canvas = canvas

        self._x1 = 0
        self._y1 = 0
        self._x2 = 0
        self._y2 = 0

        self._rubber = None 

    def on_paint(self):
        self._owner.on_paint()

    def _save_shape(self, shape):
        self._owner.add_shape(shape)
        self.on_paint()

    def on_lb_down(self, event):
        self._x1 = event.x
        self._y1 = event.y
        self._rubber = None

class PointEditor(ShapeEditor):
    def on_mouse_move(self, event):
        pass

    def on_lb_up(self, event):
        shape = PointShape()
        shape.set(event.x, event.y, event.x, event.y)
        self._save_shape(shape)

class LineEditor(ShapeEditor):
    def on_mouse_move(self, event):
        self._x2 = event.x
        self._y2 = event.y

        if self._rubber is not None:
            self._canvas.delete(self._rubber)

        self._rubber = self._canvas.create_line(self._x1, self._y1, self._x2, self._y2, fill="blue")
    
    def on_lb_up(self, event):
        self._x2 = event.x
        self._y2 = event.y

        if self._rubber is not None:
            self._canvas.delete(self._rubber)
            self._rubber = None

        shape = LineShape()
        shape.set(self._x1, self._y1, self._x2, self._y2)
        self._save_shape(shape)

class RectangleEditor(ShapeEditor):
    def on_mouse_move(self, event):
        self._x2 = event.x
        self._y2 = event.y
        
        if self._rubber is not None:
            self._canvas.delete(self._rubber)
        
        self._rubber = self._canvas.create_rectangle(self._x1, self._y1, self._x2, self._y2, outline="blue")

    def on_lb_up(self, event):
        self._x2 = event.x
        self._y2 = event.y
    
        if self._rubber is not None:
            self._canvas.delete(self._rubber)
            self._rubber = None
    
        shape = RectangleShape()
        shape.set(self._x1, self._y1, self._x2, self._y2)
        self._save_shape(shape)

class EllipseEditor(ShapeEditor):
    def _opposite_corner(self):
        return 2 * self._x1 - self._x2, 2 * self._y1 - self._y2

    def on_mouse_move(self, event):
        self._x2 = event.x
        self._y2 = event.y

        x_opp, y_opp = self._opposite_corner()

        if self._rubber is not None:
            self._canvas.delete(self._rubber)

        self._rubber = self._canvas.create_oval(x_opp, y_opp, self._x2, self._y2, outline="blue")

    def on_lb_up(self, event):
        self._x2 = event.x
        self._y2 = event.y
        x_opp, y_opp = self._opposite_corner()
        
        if self._rubber is not None:
            self._canvas.delete(self._rubber)
            self._rubber = None

        shape = EllipseShape()
        shape.set(x_opp, y_opp, self._x2, self._y2)
        self._save_shape(shape)