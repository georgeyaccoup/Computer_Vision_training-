import cv2
import numpy as np 

img = cv2.imread('D:\OpenCV course\codes\Assiut.png')
print (f"image size = {img.size}, image shape {img.shape}")


H,W=img.shape[::2]
print ("top left pixel = ", img[H-1,W-1])
B = img[H-1, W-1, 0] 
G = img[H-1, W-1, 1] 
R = img[H-1, W-1, 2] 
print(f'B={B}  G={G}  R={R}') 
cv2.waitKey(0)
cv2.destroyAllWindows()
