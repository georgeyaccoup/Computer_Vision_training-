import cv2, numpy as np

img=cv2.imread("D:\OpenCV course\codes\Assiut.png")
H,W = img.shape[:2]
print (f" hight ={H}, Width={W}")
grayImage=np.zeros((H,W), dtype= np.uint8)

for h in range (H):
    for w in range (W):
        value=0.299*img[h,w,0]+0.587*img[h,w,1]+0.114*img[h,w,2]
        grayImage[h,w]=value

cv2.imwrite(r"D:\OpenCV course\codes\assiut_gray.jpeg", grayImage, [cv2.IMWRITE_JPEG_QUALITY, 50])
cv2.waitKey(0)
cv2.destroyAllWindows()