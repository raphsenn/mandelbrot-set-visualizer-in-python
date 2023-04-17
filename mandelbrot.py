from PIL import Image

def mandelbrot(c: complex, m: int):
    zn = 0
    for i in range(1, m + 1):
        z = zn ** 2 + c
        zn = z
        if abs(z) > 2:
            return i
        elif abs(z) < 2 and m == i:
            return m

# convert complex numbers to pixels
def sample(z: complex, w: complex, x: int, y: int, sx: int, sy: int):
    new_sx = round((abs(z.real - w.real)) * (x / sx) + z.real, 2)
    new_sy = round((abs(z.imag - w.imag)) * (y / sy) + z.imag, 2)
    return (complex(new_sx, new_sy))


def color(i: int, max_i: int) -> tuple[int, int, int]:
    # Hue based on the number of iterations.
    hue = int(255 * (i / max_i))
    # Full brightness 255, except when c is part of the Mandelbrot set.
    # This makes the inside black.
    value = 255 if i < max_i else 0
    # Full saturation
    saturation = 255
    return (hue, saturation, value)


def render_mandelbrot(c: complex, w: complex, px, py, m, out_name: str):
    size = (px, py)
    img = Image.new('HSV', size)
    comp_list = []
    for x in range(size[0]):
        for y in range(size[1]):
            red = (255, 255, 255)
            komplex = mandelbrot(sample(c, w, x, y, px, py), m)
            if komplex != m and komplex is not None:
                rgb = color(komplex, 50)
                img.putpixel((x, y), rgb)
# where the picture is saved
    img.convert('RGB').save('yourpath{0}'.format(out_name), quality=95)


render_mandelbrot(-2-1j, 1+1j, 900, 600, 50, 'mandelbrot.jpg')