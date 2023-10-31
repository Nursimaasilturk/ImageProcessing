import cv2 as cv
import numpy as np

image = cv.imread('landscape-first.jpg',cv.IMREAD_GRAYSCALE)
# image = cv.imread('landscape.jpg',cv.IMREAD_GRAYSCALE)
min_pixel_value = np.min(image)
max_pixel_value = np.max(image)

new_min_value = 0
new_max_value = 255
"""
new_min_value = 0
new_max_value = 255
"""

stretched_image = np.uint8((image - min_pixel_value)/(max_pixel_value - min_pixel_value) * (new_max_value - new_min_value) + new_min_value)

cv.imshow('original image',image)
cv.imshow('stretched image',stretched_image)

cv.waitKey(0)