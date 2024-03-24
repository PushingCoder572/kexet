import os
from PIL import Image

input_dir = "images_compressed"
output_dir = "output_compressed"


def main():
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for filename in os.listdir(input_dir):
        if filename.endswith(".jpg") or filename.endswith(
            ".png"
        ):  # Add more extensions if needed
            # Open the image file
            img_path = os.path.join(input_dir, filename)
            img = Image.open(img_path)
            img.save(os.path.join(output_dir, filename), quality=20, optimize=True)


if __name__ == "__main__":
    main()
