import cv2

img = cv2.imread('laplace.jpg', 0)

blur = cv2.GaussianBlur(img, (3, 3), 0)

laplacian = cv2.Laplacian(blur, cv2.CV_64F)

laplacian1 = laplacian / laplacian.max()

cv2.imshow('Original Image', img)
cv2.imshow('Filtered Image', laplacian1)
cv2.waitKey(0)