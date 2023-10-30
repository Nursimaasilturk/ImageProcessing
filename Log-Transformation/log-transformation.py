import cv2 as cv
import numpy as np

img = cv.imread('log-transformation.jpg', cv.IMREAD_GRAYSCALE)
c = 255.0 / np.log(np.max(img) + 1)
'''
C' değeri, kullanılan bit boyutuna karşılık gelen maksimum 
çıkış değerini elde edecek şekilde seçilir.
'''
new_image = c * (np.log(1 + img))
'''Logaritmik Dönüşüm yapılır.'''
new_image = np.array(new_image, dtype = np.uint8)
'''Görüntüyü 8-bitlik veri türüne dönüştürür. Böylece elde edilen görüntü
0-255 arasındaki pixel değerlerini alabilir.
'''

cv.imshow('original image',img)
cv.imshow('new image',new_image)

cv.waitKey(0)