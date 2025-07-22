import numpy as np
from PIL import Image

def cubic_kernel(t):
    """Catmull-Rom cubic kernel"""
    a = -0.5
    abs_t = np.abs(t)
    abs_t2 = abs_t**2
    abs_t3 = abs_t**3

    if abs_t <= 1:
        return (a + 2) * abs_t3 - (a + 3) * abs_t2 + 1
    elif 1 < abs_t < 2:
        return a * abs_t3 - 5 * a * abs_t2 + 8 * a * abs_t - 4 * a
    else:
        return 0

def get_pixel(pixels, x, y):
    height, width, _ = pixels.shape
    x = min(max(0, x), width - 1)
    y = min(max(0, y), height - 1)
    return pixels[y, x]

def bicubic_interpolation(source_img, new_width, new_height):
    src_width, src_height = source_img.size
    src_pixels = np.array(source_img, dtype=float)

    target_img = Image.new("RGB", (new_width, new_height))
    tgt_pixels = target_img.load()

    scale_x = src_width / new_width
    scale_y = src_height / new_height

    for y in range(new_height):
        for x in range(new_width):
            src_x = x * scale_x
            src_y = y * scale_y

            x_int = int(np.floor(src_x))
            y_int = int(np.floor(src_y))
            dx = src_x - x_int
            dy = src_y - y_int

            interpolated_pixel = np.zeros(3)

            for m in range(-1, 3):
                for n in range(-1, 3):
                    pixel = get_pixel(src_pixels, x_int + n, y_int + m)
                    weight = cubic_kernel(n - dx) * cubic_kernel(m - dy)
                    interpolated_pixel += pixel * weight

            # Clip pixel values and assign
            interpolated_pixel = np.clip(interpolated_pixel, 0, 255)
            tgt_pixels[x, y] = tuple(interpolated_pixel.astype(np.uint8))

    return target_img