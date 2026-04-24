import cv2
import numpy as np 

img = cv2.imread('D:\OpenCV course\codes\Assiut.png') 

pixel_data = img[100, 200]  
b,g,r=img[100,200]
index_3 = img[100,200,0]
print (f"total {pixel_data}, b={b}, g={g}, r={r},index_3 {index_3}")

cv2.imshow("image",img)
print(f"Data structure type: {type(pixel_data)}") 

cv2.waitKey(0)
cv2.destroyAllWindows()