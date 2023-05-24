from PIL import Image, ImageChops

def trim(img):
    """TODO: Docstring for trim.

    :image_path: TODO
    :returns: TODO

    """
    # Trim the image to its object
    bg = Image.new(img.mode, img.size, img.getpixel((0,0)))
    diff = ImageChops.difference(img, bg)
    bbox = diff.getbbox()
    trimmed_img = img.crop(bbox)

    return trimmed_img
