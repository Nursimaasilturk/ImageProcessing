import cv2
import numpy as np

img = cv2.imread('gamma-tranformation.jpg')
"""
img = cv2.imread('gamma-tranformation.jpg', cv2.IMREAD_GRAYSCALE)
Gri görüntü 
"""
gamma = 2
img_2 = np.power(img,gamma)

gamma = 3
img_3 = np.power(img,gamma)

gamma = 4
img_4 = np.power(img,gamma)

cv2.imshow('original image',img)
cv2.imshow('gamma -> 2',img_2)
cv2.imshow('gamma -> 3',img_3)
cv2.imshow('gamma -> 4',img_4)

cv2.waitKey(0)