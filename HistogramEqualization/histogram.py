from __future__ import  print_function
from __future__ import division
import cv2
import argparse
import numpy as np
import matplotlib.pyplot as plt

parser = argparse.ArgumentParser(description='Histogram Equalization')
parser.add_argument('--input',help='Path to input image', default='histogram.jpg')
args= parser.parse_args()

src = cv2.imread(cv2.samples.findFile(args.input))
if src is None:
    print('Image does not found',args.input)
    exit(0)

src = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
hist_original, bins_original = np.histogram(src.flatten(), 256, [0, 256])
dst= cv2.equalizeHist(src)
hist_equalized, bins_equlized = np.histogram(dst.flatten(), 256, [0, 256])
#Grafiği çizme
plt.figure(figsize=(12, 6))
# Orijinal histogram
plt.subplot(1, 2, 1)
plt.plot(hist_original, color='gray')
plt.xlabel('Pixel Value')
plt.ylabel('Frequency')
plt.title('Original Image Histogram')

# Eşitleme sonrası histogram
plt.subplot(1, 2, 2)
plt.plot(hist_equalized, color='gray')
plt.xlabel('Pixel Value')
plt.ylabel('Frequency')
plt.title('Equalized Image Histogram')

cv2.imshow('Original Image',src)
cv2.imshow('Equalized Image',dst)
plt.show()
cv2.waitKey()
