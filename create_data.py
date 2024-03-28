import cv2
import os
import shutil
import numpy as np

# Define the path to the original dataset folder
original_folder_path = './original_data/'

# Define the paths for the four new folders
compression_folder_path = './compression/'
histogram_eq_folder_path = './histogram_eq/'
noise_reduction_folder_path = './noise_reduction/'
normalization_folder_path = './normalization'

# Function to create a copy of the original folder structure
def copy_folder_structure(src, dst):
    if not os.path.exists(dst):
        os.makedirs(dst)
    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dst, item)
        if os.path.isdir(s):
            copy_folder_structure(s, d)
        else:
            shutil.copy2(s, d)

# Function to apply compression (JPEG quality adjustment)
def apply_compression(image_path, output_path):
    image = cv2.imread(image_path)
    # Adjust the quality value as needed (0-100, where 100 is max quality)
    cv2.imwrite(output_path, image, [int(cv2.IMWRITE_JPEG_QUALITY), 50])

# Function to apply histogram equalisation
def apply_histogram_eq(image_path, output_path):
    image = cv2.imread(image_path, 0)  # Read in grayscale
    eq_image = cv2.equalizeHist(image)
    cv2.imwrite(output_path, eq_image)

# Function to apply noise reduction (Gaussian blur as an example)
def apply_noise_reduction(image_path, output_path):
    image = cv2.imread(image_path)
    blur_image = cv2.GaussianBlur(image, (5, 5), 0)
    cv2.imwrite(output_path, blur_image)

# Function to apply normalization
def apply_normalization(image_path, output_path):
    image = cv2.imread(image_path)
    norm_image = cv2.normalize(image, None, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_32F)
    cv2.imwrite(output_path, (norm_image * 255).astype(np.uint8))

# Function to process all images in a folder
def process_images(src_folder, dst_folder, process_function):
    for root, dirs, files in os.walk(src_folder):
        for file in files:
            if file.lower().endswith(('png', 'jpg', 'jpeg')):
                src_path = os.path.join(root, file)
                relative_path = os.path.relpath(src_path, src_folder)
                dst_path = os.path.join(dst_folder, relative_path)
                process_function(src_path, dst_path)

# Copy the folder structure and process images for each modification
for folder, function in [(compression_folder_path, apply_compression),
                         (histogram_eq_folder_path, apply_histogram_eq),
                         (noise_reduction_folder_path, apply_noise_reduction),
                         (normalization_folder_path, apply_normalization)]:
    copy_folder_structure(original_folder_path, folder)
    process_images(original_folder_path, folder, function)

print("Processing complete.")
