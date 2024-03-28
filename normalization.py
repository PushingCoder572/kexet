import os
import cv2 as cv
import numpy as np

#input_dir = "../datasets/Parkeringsskylt.v6i.yolov8/train/images"
#output_dir = "../datasets/Parkeringsskylt.v6i.yolov8/train/normalization_images/"

#input_dir = "../datasets/Parkeringsskylt.v6i.yolov8/test/images"
#output_dir = "../datasets/Parkeringsskylt.v6i.yolov8/test/normalization_images/"

input_dir = "../datasets/Parkeringsskylt.v6i.yolov8/valid/images"
output_dir = "../datasets/Parkeringsskylt.v6i.yolov8/valid/normalization_images/"


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
            norm_img = np.zeros((800, 800))
            final_img = cv.normalize(img, norm_img, 0, 255, cv.NORM_MINMAX)

            cv.imwrite(os.path.join(output_dir, filename), final_img)


if __name__ == "__main__":
    main()
