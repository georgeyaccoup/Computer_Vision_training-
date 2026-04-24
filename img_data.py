import cv2
import numpy as np
img = cv2.imread('D:\OpenCV course\codes\Assiut.png')

print ("image shape : ", img.shape)
print ("image channels: ", img.ndim)
print ("array type:", img.dtype)
print("image size", img.size) 

H, W, C=img.shape
print (f"H= {H}, W= {W}, and C={C}")

CH_1 = img.shape[ : :1]
print ("\n CH_1= ", CH_1)

