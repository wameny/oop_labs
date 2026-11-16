from editor import PointEditor, LineEditor, RectangleEditor, EllipseEditor

MAX_SHAPES = 126

class ShapeObjectsEditor:
    def __init__(self, canvas):
        self._canvas = canvas
        self._shapes = [None] * MAX_SHAPES
        self._count = 0
        self._editor = None
        self._mode = ""

    def start_point_editor(self):
        self.shape_editor(PointEditor, 'point')

    def start_line_editor(self):
        self.shape_editor(LineEditor, 'line')

    def start_rectangle_editor(self):
        self.shape_editor(RectangleEditor, 'rect')

    def start_ellipse_editor(self):
        self.shape_editor(EllipseEditor, 'ellipse')

    def on_lb_down(self, event):
        if self._editor is not None:
            self._editor.on_lb_down(event)

    def on_lb_up(self, event):
        if self._editor is not None:
            self._editor.on_lb_up(event)

    def on_mouse_move(self, event):
        if self._editor is not None:
            self._editor.on_mouse_move(event)

    def add_shape(self, shape):
        if self._count < MAX_SHAPES:
            self._shapes[self._count] = shape
            self._count += 1

    def on_paint(self):
        self._canvas.delete("all")
        for i in range(self._count):
            self._shapes[i].show(self._canvas)

    def current_mode(self):
        return self._mode

    def shape_editor(self, editor_class, mode):
        self._editor = editor_class(self, self._canvas)
        self._mode = mode