# Import libraries
import cv2
import numpy as np

# -------- IMAGE 1 --------
img = cv2.imread("D:\OpenCV course\codes\elephant.jpg")

img[100, 200] = [0, 0, 255]
cropped=img[10:100,20:100]
img[100:300, 50:80] = [0, 255, 0] 
H, W = img.shape[:2]  

img[:, W//2] = [255, 255, 255]

cx, cy, r = W//2, H//2, 30 
y, x = np.ogrid[:H, :W] 
mask = (x-cx)**2 + (y-cy)**2 <= r**2
img[mask] = [255, 255, 255] 

cv2.imshow("test", img)
cv2.imshow("cropped", cropped)

cv2.waitKey(0)
cv2.destroyAllWindows()