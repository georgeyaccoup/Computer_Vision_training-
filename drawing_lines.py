import cv2, numpy as np, math
x_index = 200
y_index = 200
img = np.zeros((y_index, x_index), dtype=np.uint8)

for i in range(x_index):
    img[i, i] = 255 

for i in range(x_index):
    img[x_index - 1 - i, i] = 255

cy, cx = y_index // 2, x_index // 2
r = 50

for i in range(x_index):
    x = i
    value = r**2 - ((x - cx)**2)

    if value >= 0:
        y_offset = math.sqrt(value)

        y1 = int(cy + y_offset)
        y2 = int(cy - y_offset)

        if 0 <= y1 < y_index:
            img[y1, x] = 255
        if 0 <= y2 < y_index:
            img[y2, x] = 255

cv2.imshow("img", img)
cv2.waitKey(0)
cv2.destroyAllWindows()