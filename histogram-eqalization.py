import os
import cv2 as cv


input_dir = "images_histogramequalization"
output_dir = "output_histogramequalization"


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

            clahe = cv.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
            cl1 = clahe.apply(img)

            cv.imwrite(os.path.join(output_dir, filename), cl1)


if __name__ == "__main__":
    main()
