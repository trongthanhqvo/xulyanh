import cv2
import numpy as np

# 1
I = cv2.imread("./anhthi/Coins.jpg")
# cv2.imshow("I", I)

# 2
Ig = np.zeros((I.shape[0], I.shape[1]), dtype='uint8')
for i in range(0, I.shape[0]):
    for j in range(0, I.shape[1]):
        Ig[i][j] = int(0.39 * I[i][j][2] + 0.5 * I[i][j][1] + 0.11 * I[i][j][0])
print("muc xam trung binh:", np.mean(Ig))
# cv2.imshow("Ig", Ig)

# 3
h = Ig.shape[0]
w = Ig.shape[1]
y = 100
x = 120

print("Cac gia tri mua xam ma tran 5x5:")
for i in range(-2, 3):
    for j in range(-2, 3):
        if ((y + i) >= 0) & ((y + i) <= h - 1) & ((x + j) >= 0) & ((x + j) <= w - 1):
            print("matrix[{}][{}]={}".format(i, j, Ig[y+i][x+j]))
        else:
            print("matrix[{}][{}]={}".format(i, j, "vuot qua"))

# 4
Ie = cv2.Canny(Ig, 0, 255)
# cv2.imshow("Ie", Ie)
if Ie[y][x] == 255:
    print("La diem bien cua Ig")
else:
    print("Khong la diem bien cua Ig")

# 5
thresh, Ib = cv2.threshold(Ig, 0, 255, cv2.THRESH_OTSU)
# cv2.imshow("Ib", Ib)

contours, con = cv2.findContours(Ib, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(I, contours, -1, (0, 255, 0), 2 )  # green
# cv2.imshow("contours I", I)
cv2.waitKey(0)
