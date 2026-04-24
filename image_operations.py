import cv2
import numpy as np 

img = cv2.imread("D:\OpenCV course\codes\colors.png",1)  # colored photo attribute "1 -> cv2.IMREAD_COLOR"
cv2.imshow("before", img)

H,W = img.shape[:2]
print("H=", H, "- W=", W)

roi=img[0:150, 0:150]
print(roi.shape)

top_left = img[:H//2, :W//2] 
cy, cx = H//2, W//2 

size = 100 
center_roi = img[cy-size:cy+size, cx-size:cx+size]
roi_copy = img[100:300, 50:350].copy() 

roi_copy[:] = [0, 255, 0] 

cv2.waitKey(0)
cv2.destroyAllWindows()
