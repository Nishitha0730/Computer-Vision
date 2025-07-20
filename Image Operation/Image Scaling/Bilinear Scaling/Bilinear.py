from PIL import Image
import numpy as np

def bilinear_interpolation(source_img, new_width, new_height):
    src_width, src_height = source_img.size
    src_pixels = np.array(source_img, dtype=float)

    target_img = Image.new("RGB", (new_width, new_height))
    tgt_pixels = target_img.load()

    for y in range(new_height):
        for x in range(new_width):
            # Map coordinates
            src_x = x * (src_width - 1) / (new_width - 1)
            src_y = y * (src_height - 1) / (new_height - 1)

            x0 = int(np.floor(src_x))
            x1 = min(x0 + 1, src_width - 1)
            y0 = int(np.floor(src_y))
            y1 = min(y0 + 1, src_height - 1)

            dx = src_x - x0
            dy = src_y - y0

            # Get pixels
            Q11 = src_pixels[y0][x0]
            Q21 = src_pixels[y0][x1]
            Q12 = src_pixels[y1][x0]
            Q22 = src_pixels[y1][x1]

            # Interpolate RGB separately
            interp_pixel = (
                (1 - dx) * (1 - dy) * Q11 +
                dx * (1 - dy) * Q21 +
                (1 - dx) * dy * Q12 +
                dx * dy * Q22
            )

            tgt_pixels[x, y] = tuple(map(int, interp_pixel))

    return target_img
