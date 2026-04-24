import cv2
import numpy as np 

img = cv2.imread('D:\OpenCV course\codes\colors.png') 
H, W = img.shape[:2]
   
# Resize to exact dimensions  
resized = cv2.resize(img, (320, 240)) 
print(resized.shape)
   
# Resize by scale factor (keep aspect ratio)  
half   = cv2.resize(img, (W//2, H//2)) 
double = cv2.resize(img, (W*2,  H*2)) 
   
# Resize to fixed width, compute height  
new_w  = 400 
scale  = new_w / W 
new_h  = int(H * scale) 
resized= cv2.resize(img, (new_w, new_h)) 

cv2.imshow("resized",resized)
cv2.waitKey(0)
cv2.destroyAllWindows()
