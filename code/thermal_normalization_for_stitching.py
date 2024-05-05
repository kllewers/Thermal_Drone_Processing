#packages needed for analysis
import cv2
import numpy as np
from scipy import stats
from matplotlib import pyplot as plt
import piexif
from PIL import Image

#for extracting the EXIF data/metadata
def get_exif_data(image_path):
    img = Image.open(image_path)
    exif_data = img.info['exif']
    return exif_data

def save_exif_data(image_path, new_image, exif_data):
    new_image_PIL = Image.fromarray(new_image)
    new_image_PIL.save(image_path, "JPEG", exif=exif_data)

#execute the function
#step 1, read the original image
original_image_path = ('/Users/kitlewers/Desktop/drone_project_adler/original_images/DJI_0860.JPG')
img = cv2.imread(original_image_path)

#step #2, convert to grayscale
gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#step #3, extract the exif data
exif_data = get_exif_data(original_image_path)

#step #4, create a new path for image to be saved to and run final function
new_image_path = '/Users/kitlewers/Desktop/drone_project_adler/converted_image/DJI_0860.JPG'
save_exif_data(new_image_path, gray_image, exif_data)

folder_path = '/Users/kitlewers/Desktop/drone_project_adler/original_images'







