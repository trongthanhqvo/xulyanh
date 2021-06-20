import cv2
import numpy as np

# 1
I = cv2.imread("./anhthi/anh5.jpg")
# cv2.imshow("I", I)

# 2
Ig = np.zeros((I.shape[0], I.shape[1]), dtype='uint8')
for i in range(0, I.shape[0]):
    for j in range(0, I.shape[1]):
        Ig[i][j] = int(0.39 * I[i][j][2] + 0.5 * I[i][j][1] + 0.11 * I[i][j][0])
print("muc xam lon nhat:", np.max(Ig))
# cv2.imshow("Ig", Ig)


# 3
print("muc xam nho nhat cua Ig:", np.min(Ig))
print("muc xam lon nhat cua Ig:", np.max(Ig))
print("muc xam trung binh cua Ig:", np.mean(Ig))

# 4
thresh, Ib = cv2.threshold(Ig, 0, 255, cv2.THRESH_OTSU)
# cv2.imshow("Ib", Ib)

# 5
contours, con = cv2.findContours(Ib, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# tìm ra chu vi lớn nhất
max_chuvi = 0.0
for ct in contours:
    if max_chuvi <= cv2.arcLength(ct, True):
        max_chuvi = cv2.arcLength(ct, True)

contours_max = []
for ct in contours:
    if cv2.arcLength(ct, True) > (max_chuvi / 3.0):
        contours_max = ct
        cv2.drawContours(I, [contours_max], -1, (0, 255, 0), 3)

cv2.imshow("contours cv > cv/3", I)
cv2.waitKey(0)