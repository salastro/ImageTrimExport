"""TODO: Docstring for trim.py."""
from PIL import Image, ImageChops

def trim_to_object(image):
    """TODO: Docstring for trim.

    :image_path: TODO
    :returns: TODO

    """
    # Trim the image to its object
    background = Image.new(image.mode, image.size, image.getpixel((0,0)))
    diff = ImageChops.difference(image, background)
    bbox = diff.getbbox()
    trimmed_img = image.crop(bbox)

    return trimmed_img
