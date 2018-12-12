import io
import cairo
from IPython.display import Image

def surface_to_image(surface):
    buf = io.BytesIO()
    surface.write_to_png(buf)
    data = buf.getvalue()
    buf.close()
    return Image(data=data)