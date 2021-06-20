import cv2
import numpy as np

# 1
I = cv2.imread("./anhthi/clother1.jpg")
# cv2.imshow("I", I[:, :, 0])

# 2
Ihsv = cv2.cvtColor(I, cv2.COLOR_BGR2HSV)
h = Ihsv.shape[0]
w = Ihsv.shape[1]
y = 10
x = 20
print("Cac gia tri diem anh")
for i in range(-2, 3):
    for j in range(-2, 3):
        if ((y + i) >= 0) & ((y + i) <= h - 1) & ((x + j) >= 0) & ((x + j) <= w - 1):
            print("matrix[{}][{}]={}".format(i, j, Ihsv[y + i][x + j]))
        else:
            print("matrix[{}][{}]={}".format(i, j, "vuot qua"))
# cv2.imshow("Ihsv", Ihsv[:, :, 1])

# 3
thresh, Ib = cv2.threshold(Ihsv[:, :, 1], 0, 255, cv2.THRESH_OTSU)
# cv2.imshow("Ib", Ib)

# 4
Im = cv2.blur(Ihsv[:, :, 1], (5, 5))
# cv2.imshow("Im", Im)

# 5
contours, con = cv2.findContours(Im, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(I, contours, -1, (0, 0, 255), 2)
cv2.imshow("Contours I", I)
cv2.waitKey(0)
