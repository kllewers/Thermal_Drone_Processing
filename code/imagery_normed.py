import cv2
image = cv2.imread('/Users/kitlewers/Desktop/drone_project_adler/images/DJI_0862.JPG')

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

