import numpy as np
import cv2

# 1
I = cv2.imread("./anhthi/anh5.jpg")
cv2.imshow("  I", I)

# 2
Ig = np.zeros((I.shape[0], I.shape[1]), dtype="uint8")
for i in range(0, Ig.shape[0]):
    for j in range(0, Ig.shape[1]):
        Ig[i][j] = int(0.39 * I[i][j][2] + 0.5 * I[i][j][1] + 0.11 * I[i][j][0])
print("Muc xam trung cua anh Ig", np.mean(Ig))
# cv2.imshow("Ig convert", Ig)

# 3
Ie = cv2.Canny(Ig, 0, 255)
# cv2.imshow("Ie", Ie)

# 4
y = 100
x = 300
if Ig[y][x] == 255:
    print("là điểm biên")
else:
    print("không là biên")


# 5
thresh, Ib = cv2.threshold(Ig, 0, 255, cv2.THRESH_OTSU)
# cv2.imshow("Ib", Ib)


# 6
contours, con = cv2.findContours(Ib, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

max_area = 0.0
for ct in contours:
    if max_area <= cv2.contourArea(ct):
        max_area = cv2.contourArea(ct)

contours_max = []
for ct in contours:
    if max_area >= max_area/5.0:
        contours_max = ct
        cv2.drawContours(I, [contours_max], -1, (0, 255, 0), 2)  # green
# cv2.imshow("Contours I", I)

cv2.waitKey(0);