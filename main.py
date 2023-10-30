from __future__ import print_function
""" python2 deki print komutunu python3'e uyarlı bir şekilde getirmek için kullanılır """
from builtins import  input
""" python2 deki input fonksiyonunu python3'e uyarlanması için kullanılır."""
import cv2 as cv
import numpy as np
import argparse

#Read image by user
parser = argparse.ArgumentParser(description='Changing the contrast and brightness of an image!')
"""Argument Parser'in açıklamasını gösterir. Bu yapı kullanıcıdan input almaya yarar."""
parser.add_argument('--input',help='Path to input image',default='landscape.jpg')
"""__input:kullanıcıdan alınacak olan argümanın(değişken gibi) adıdır.help:argümanın ne ile ilgili olduğunu gösterir.
default: kullanıcı eğer herhangi bir değer girmezse bu resmin kullanılacağı gösterilir."""
args = parser.parse_args()
"""argümanı nesneye dönüştürerek kullanıcının erişmesini sağlar."""

image = cv.imread(cv.samples.findFile(args.input))
"""Dosya yoluyla resmi bulur ve cv kullanarak bu resmi matrislere dönüştürüp değişkenin içine atar."""
if image is None:
    print('Resim açılamıyor', args.input)
    exit(0)
"""Eğer resmi bulamazsa gerekli mesajı gönderir."""

new_image = np.zeros(image.shape,image.dtype)
"""orijinal görüntünün aynı boyut ve veri türüne sahip boş bir matris oluşturur.
 Yani, yeni görüntüyü depolamak için kullanılacak bir boş alan yaratılır. 
 Bu, işlem sonucunda değiştirilmiş görüntünün saklanacağı yerdir."""

alpha = 1.0
beta = 0
"""Default contrast ve brightness değerleri"""
print("Basic Linear Transform")
print("-----------------------")
try:
    alpha= float(input("* Enter the alpha value [1.0-3.0]: "))
    beta = float(input("* Enter the beta value [0-100]: "))
except ValueError:
    print("Error,not a number")
"""Kullanıcıdan contrast ve brightness değerleri alınır belirlenen aralıklarda"""

for y in range(image.shape[0]):
    for x in range(image.shape[1]):
        for z in range(image.shape[2]):
            new_image[y,x,z] = np.clip(alpha*image[y,x,z] + beta,0,255)
"""Girilen alpha ve beta değerlerine göre resim ayarlanır."""

cv.imshow('Original Image',image)
cv.imshow('New Image',new_image)
"""Orjinal ve değiştirilmiş resim ekranda gösterilir."""
cv.waitKey(0)
"""Kullanıcı herhangi bir tuşa basarak işlemi sonlandırır.2"""
cv.destroyAllWindows()