#packages needed for analysis
import cv2
import numpy as np
from scipy import stats
from matplotlib import pyplot as plt


image = cv2.imread('/Users/kitlewers/Desktop/drone_project_adler/images/DJI_0862.JPG')
image2 = cv2.imread('/Users/kitlewers/Desktop/drone_project_adler/images/DJI_0860.JPG')

# Convert it to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray_image2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)

# Display the grayscale image
cv2.imshow('Above Canopy', gray_image)
cv2.imshow('Below Canopy', gray_image2)

# Wait for a key press to close the window
cv2.waitKey(0)

# Normalize the images to range 0-1
normalized_image = gray_image / 255.0
normalized_image2 = gray_image2 / 255.0


# Calculate statistics for the first image
mean1 = np.mean(normalized_image)
median1 = np.median(normalized_image)


# Calculate statistics for the second image
mean2 = np.mean(normalized_image2)
median2 = np.median(normalized_image2)


# Print statistics
print("Statistics for 'Above Canopy':")
print("Mean:", mean1)
print("Median:", median1)

print("\nStatistics for 'Below Canopy':")
print("Mean:", mean2)
print("Median:", median2)

# Use matplotlib to display the images
plt.subplot(1, 2, 1)
plt.imshow(normalized_image, cmap='gray')
plt.title('Above Canopy Normalized')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(normalized_image2, cmap='gray')
plt.title('Below Canopy Normalized')
plt.axis('off')

plt.show()
