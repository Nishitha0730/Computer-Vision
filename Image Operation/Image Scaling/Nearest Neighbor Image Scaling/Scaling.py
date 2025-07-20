from PIL import Image

# https://courses.cs.vt.edu/~masc1044/L17-Rotation/ScalingNN.html
# https://theailearner.com/tag/image-interpolation-opencv-python/

def nearest_neighbor_scaling(source_img, new_width, new_height):
    """
    Scales an image using the nearest neighbor algorithm.

    Parameters:
        source_img (PIL.Image): The input image.
        new_width (int): The desired width of the scaled image.
        new_height (int): The desired height of the scaled image.

    Returns:
        PIL.Image: The scaled output image.
    """
    src_width, src_height = source_img.size
    target_img = Image.new("RGB", (new_width, new_height))

    src_pixels = source_img.load()
    tgt_pixels = target_img.load()

    for y in range(new_height):
        for x in range(new_width):
            src_x = int(round(x / new_width * src_width))
            src_y = int(round(y / new_height * src_height))
            src_x = min(src_x, src_width - 1)
            src_y = min(src_y, src_height - 1)
            tgt_pixels[x, y] = src_pixels[src_x, src_y]

    return target_img
