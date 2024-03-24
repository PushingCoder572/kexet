import os
import cv2 as cv


input_dir = "images_noise_reduction"
output_dir = "output_noise_reduction"


def main():
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for filename in os.listdir(input_dir):
        if filename.endswith(".jpg") or filename.endswith(
            ".png"
        ):  # Add more extensions if needed
            # Open the image file
            img_path = os.path.join(input_dir, filename)
            img = cv.imread(img_path, cv.IMREAD_UNCHANGED)
            assert (
                img is not None
            ), "file could not be read, check with os.path.exists()"

            dst = cv.fastNlMeansDenoisingColored(img, None, 10, 10, 7, 21)
            cv.imwrite(os.path.join(output_dir, filename), dst)


if __name__ == "__main__":
    main()
