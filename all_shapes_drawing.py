import cv2
import numpy as np

# Create black image (1000x1000)
img = np.zeros((1000, 1000,3), dtype=np.uint8)

# 1. LINE
# cv2.line(image, start_point, end_point, color, thickness)
cv2.line(img, (30, 30), (250, 250), (255,0,0), 2)

# 2. RECTANGLE
# cv2.rectangle(image, top_left, bottom_right, color, thickness)
cv2.rectangle(img, (300, 30), (600, 250), (255,255,255), 2)

# 3. FILLED RECTANGLE
# cv2.rectangle(image, top_left, bottom_right, color, thickness=-1)
cv2.rectangle(img, (650, 30), (950, 250), (255,255,255), -1)

# 4. CIRCLE
# cv2.circle(image, center, radius, color, thickness)
cv2.circle(img, (150, 500), 100, (255,255,255), 2)

# 5. FILLED CIRCLE
# cv2.circle(image, center, radius, color, thickness=-1)
cv2.circle(img, (500, 500), 100, (255,255,255), -1)

# 6. ELLIPSE
# cv2.ellipse(image, center, axes, angle, startAngle, endAngle, color, thickness)
cv2.ellipse(img, (850, 500), (100,50), 0, 0, 360, (255,255,255), 2)

# 7. TRIANGLE (POLYLINES)
# cv2.polylines(image, [points], isClosed, color, thickness)
pts = np.array([[150,750],[80,950],[220,950]], np.int32)
cv2.polylines(img, [pts], True, (255,255,255), 2)

# 8. FILLED TRIANGLE
# cv2.fillPoly(image, [points], color)
pts2 = np.array([[500,750],[430,950],[570,950]], np.int32)
cv2.fillPoly(img, [pts2], (255,255,255))

# 9. ARROWED LINE
# cv2.arrowedLine(image, start_point, end_point, color, thickness)
cv2.arrowedLine(img, (700, 750), (950, 950), (255,255,255), 2)

# 10. TEXT
# cv2.putText(image, text, position, font, fontScale, color, thickness)
cv2.putText(img, "OpenCV", (350, 980),
            cv2.FONT_HERSHEY_SIMPLEX, 1.5, (255,255,255), 2)

# Show result
cv2.imshow("Shapes", img)
cv2.waitKey(0)
cv2.destroyAllWindows()