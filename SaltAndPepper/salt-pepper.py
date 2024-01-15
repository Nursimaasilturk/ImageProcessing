import cv2
import numpy as np

def add_salt_and_pepper_noise(image, salt_prob, pepper_prob):
    output = np.copy(image)

    salt_mask = np.random.rand(*image.shape[:2]) < salt_prob
    output[salt_mask] = 255

    pepper_mask = np.random.rand(*image.shape[:2]) < pepper_prob
    output[pepper_mask] = 0

    return output

image_path = 'tac-mahal.jpg'
image = cv2.imread(image_path)

salt_and_pepper_image = add_salt_and_pepper_noise(image, salt_prob=0.2, pepper_prob=0.1)

cv2.imshow('Original Image', image)
cv2.imshow('Salt and Pepper Noise', salt_and_pepper_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
