import cairo
import numpy as np

class Shape:
    def __init__(self, stroke = None, fill = None):
        self.stroke = stroke
        self.fill = fill
        
    def draw(self, ctx):
        draw_stroke(ctx, self.stroke)
        draw_fill(ctx, self.fill)

class Circle(Shape):
    def __init__(self, cx, cy, radius, **kwargs):
        super().__init__(**kwargs)
        self.args = [cx, cy, radius]
        
    def draw(self, ctx):
        ctx.arc(*self.args, 0, 2 * np.pi)
        super().draw(ctx)

class Rectangle(Shape):
    def __init__(self, x, y, w, h, **kwargs):
        super().__init__(**kwargs)
        self.args = [x, y, w, h]
        
    def draw(self, ctx):
        ctx.rectangle(*self.args)
        super().draw(ctx)

class ShapeGroup:
    def __init__(self, shapes):
        """
        shapes: dict of shapes
        """
        self.shapes = shapes
        
    def draw(self, ctx):
        shapes = self.shapes
        for key in shapes:
            value = shapes[key]
            value.draw(ctx)
            
class Transform:
    def __init__(self, children = None, translation = None, rotation = None, scale = None):
        """
        translation = (tx, ty)
        rotation = angle
        scale = (sx, sy)
        """
        self.translation = translation
        self.rotation = rotation
        self.scale = scale
        self.children = children
        
    def draw(self, ctx):
        if self.children is not None:
            ctx.save()
            if self.translation is not None:
                ctx.translate(*self.translation)
            if self.rotation is not None:
                ctx.rotate(np.radians(self.rotation))
            if self.scale is not None:
                ctx.scale(*self.scale)
            self.children.draw(ctx)
            ctx.restore()

def draw_stroke(ctx, stroke = None):
    if stroke is None:
        return
    
    thickness, color = stroke
    ctx.set_line_width(thickness)
    ctx.set_source_rgb(*color)
    ctx.stroke()
    
def draw_fill(ctx, fill = None):
    if fill is None:
        return
    ctx.set_source_rgb(*fill)
    ctx.fill()   