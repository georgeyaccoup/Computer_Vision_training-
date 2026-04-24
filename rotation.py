import cv2
import numpy as np 

img = cv2.imread("D:\OpenCV course\codes\colors.png",1) 
flipped_v  = cv2.flip(img,  0)
flipped_h  = cv2.flip(img,  1) 
flipped_hv = cv2.flip(img, -1) 

cv2.imshow("rotated", img)
cv2.imshow("flipped_v", flipped_v)
cv2.imshow("flipped_h", flipped_h)
cv2.imshow("flipped_hv", flipped_hv)

H, W = img.shape[:2]  
center = (W//2, H//2) 
angle  = 45 
scale  = 1.0 
   
M = cv2.getRotationMatrix2D(center, angle, scale) 
print ("M= ", M)
rotated = cv2.warpAffine(img, M, (W, H)) 

cv2.imshow("rotated", rotated)

# Rotate 90° clockwise (faster than warpAffine)  
r90 = cv2.rotate(img, 
cv2.ROTATE_90_CLOCKWISE) 
r180= cv2.rotate(img, cv2.ROTATE_180)  
r270= cv2.rotate(img, 
cv2.ROTATE_90_COUNTERCLOCKWISE)  
   
# Expand canvas to avoid cropping corners  
cos_a = abs(M[0,0]) ; sin_a = abs(M[0,1])  
new_W = int(H*sin_a + W*cos_a) 
new_H = int(H*cos_a + W*sin_a) 
M[0,2] += (new_W/2) - center[0] 
M[1,2] += (new_H/2) - center[1]  
rotated_full = cv2.warpAffine(img, M, (new_W, new_H))
cv2.imshow("rotated_full", rotated_full)
cv2.waitKey(0)
cv2.destroyAllWindows()
