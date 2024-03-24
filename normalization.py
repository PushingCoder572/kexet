import os
from PIL import Image
import numpy as np

input_dir = "images_normalized"
output_dir = "output_normalized"


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

            # Convert the image data to a NumPy array
            img_array = np.array(img)

            # Normalize the pixel values to the range 0-1
            img_array = img_array.astype("float32") / 255.0

            # Convert the normalized array back to an image
            normalized_img = Image.fromarray(img_array)

            # Save the normalized image to the output directory
            normalized_img.save(os.path.join(output_dir, filename))


if __name__ == "__main__":
    main()
