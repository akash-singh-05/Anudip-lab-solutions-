import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image in grayscale
image = cv2.imread(r'C:\Users\akash\Downloads\dog.jpg', cv2.IMREAD_GRAYSCALE)

# Apply Sobel filter on the x-axis and y-axis
sobel_x = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=5)
sobel_y = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=5)

# Calculate the magnitude of the gradients
sobel_combined = np.sqrt(sobel_x**2 + sobel_y**2)

# Display the original image and the filtered image
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.imshow(image, cmap='gray')
plt.title('Original Image')

plt.subplot(1, 2, 2)
plt.imshow(sobel_combined, cmap='gray')
plt.title('Sobel Filter Applied')

plt.show()
