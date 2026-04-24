import cv2, numpy as np, math

x_index = 500
y_index = 500

img = np.zeros((y_index, x_index), dtype=np.uint8)
cv2.imshow("img", img)
for i in range(50, 301):
    img[i, i] = 255

cy, cx = 100, 100
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