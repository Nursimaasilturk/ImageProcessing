import cv2
import numpy as np

image = cv2.imread('kapadokya-pasa-baglari.jpeg', cv2.IMREAD_GRAYSCALE)

sobel_x = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)
sobel_y = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)

sobel_x = np.abs(sobel_x)
sobel_y = np.abs(sobel_y)

sobel_result = cv2.addWeighted(sobel_x, 0.5, sobel_y, 0.5, 0)

cv2.imshow('Original Image', image)
cv2.imshow('Filtered Image', sobel_result)
cv2.waitKey(0)
cv2.destroyAllWindows()
