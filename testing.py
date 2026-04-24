import cv2, numpy as np

img = cv2.imread("D:\OpenCV course\codes\colors.png")
print("the shape is ", img.shape)
print("the ndim is ", img.ndim)
print("the type is ", img.dtype)


cv2.imshow("line", img)
cv2.waitKey(20000)
cv2.destroyAllWindows()



