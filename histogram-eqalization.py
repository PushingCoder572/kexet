import os
import cv2 as cv


#input_dir = "../datasets/Parkeringsskylt.v6i.yolov8/train/images"
#output_dir = "../datasets/Parkeringsskylt.v6i.yolov8/train/histogram-eqalization_images/"

#input_dir = "../datasets/Parkeringsskylt.v6i.yolov8/test/images"
#output_dir = "../datasets/Parkeringsskylt.v6i.yolov8/test/histogram-eqalization_images/"

input_dir = "../datasets/Parkeringsskylt.v6i.yolov8/valid/images"
output_dir = "../datasets/Parkeringsskylt.v6i.yolov8/valid/histogram-eqalization_images/"


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

            # convert from RGB color-space to YCrCb
            ycrcb_img = cv.cvtColor(img, cv.COLOR_BGR2YCrCb)

            # equalize the histogram of the Y channel
            ycrcb_img[:, :, 0] = cv.equalizeHist(ycrcb_img[:, :, 0])

            # convert back to RGB color-space from YCrCb
            equalized_img = cv.cvtColor(ycrcb_img, cv.COLOR_YCrCb2BGR)

            cv.imwrite(os.path.join(output_dir, filename), equalized_img)


if __name__ == "__main__":
    main()
