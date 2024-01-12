import cv2 as cv


img = cv.imread('amasra.jpeg')
assert img is not None, "file could not be read, check with os.path.exists()"

blur = cv.GaussianBlur(img,(5,5),0)

cv.imshow('Original Image',img)
cv.imshow('Filtered Image',blur)
cv.waitKey(0)
