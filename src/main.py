import os
from PIL import Image, ImageChops
from trim import trim

# Load the image
INPUT_PATH="input_folder/"
OUTPUT_PATH="output_folder/"

def main():
    """TODO: Docstring for main.
    :returns: TODO

    """
    # Get all images in path
    images = [f for f in os.listdir(INPUT_PATH) if
              os.path.isfile(os.path.join(INPUT_PATH, f))]
    for image in images:
        img = Image.open(INPUT_PATH+image)
        trimmed_img = trim(img)
        trimmed_img.save(OUTPUT_PATH+image)

if __name__ == "__main__":
    main()
