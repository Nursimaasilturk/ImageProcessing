import cv2
import cv2 as cv
import numpy as np

img = cv.imread('negative.jpg')
"""Resmi yükledik"""
print(img.dtype)
"""Görüntünün veri türünü yazdırıyoruz."""
negative_img = 255 - img
""""Max-intensity çıkartıp negatif görüntüyü elde ediyoruz."""
cv2.imshow('original',img)
cv2.imshow('negative',negative_img)
cv2.waitKey(0)