import cv2
import numpy as np
from matplotlib import pyplot as plt

# 1
I = cv2.imread("./anhthi/hat1.PNG")
# cv2.imshow("Image", I)

# 2
Ihsv = cv2.cvtColor(I, cv2.COLOR_BGR2HSV)
print("Muc sang lon nhat cua kenh S:", np.max(Ihsv[:, :, 1]))
print("Muc sang nho nhat cua kenh S:", np.min(Ihsv[:, :, 1]))

# cv2.imshow("Ihsv kenh V", Ihsv[:, :, 2])


# 3
hist = cv2.calcHist(Ihsv[:, :, 2], channels=[2], mask=None,histSize=[256], ranges=[0, 256])
plt.plot(hist)
plt.title('Histogram của kênh anh S của ảnh Ihsv')
# plt.show()

# 4

Is = cv2.medianBlur(Ihsv[:, :, 2], 3)
# cv2.imshow("lam tron kenh V", Is)

# 5
Igray = cv2.cvtColor(I, cv2.COLOR_BGR2GRAY)
thresh, Ib = cv2.threshold(Igray, 0, 255, cv2.THRESH_OTSU)
# cv2.imshow("Anh nhi phan Ib", Ib)

contours, con = cv2.findContours(Ib, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
max_s = 0.0
contours_max_s = []

for ct in contours:
    if max_s <= cv2.contourArea(ct):
        max_s = cv2.contourArea(ct)
        contours_max_s = ct
cv2.drawContours(I, [contours_max_s], -1, (0, 255, 0), 3)  # green
cv2.imshow("Contours dien tich max", I)


cv2.waitKey(0)