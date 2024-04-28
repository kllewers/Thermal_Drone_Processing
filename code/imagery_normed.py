import cv2
image = cv2.imread('/Users/kitlewers/Desktop/drone_project_adler/images/DJI_0862.JPG')

# Convert it to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Display the grayscale image
cv2.imshow('Grayscale Image', gray_image)

# Wait for a key press to close the window
cv2.waitKey(0)


