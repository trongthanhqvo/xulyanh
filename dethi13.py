import cv2
import numpy as np
from matplotlib import pyplot as plt

# 11
I = cv2.imread("./anhthi/hat1.PNG")
# cv2.imshow("I", I)

# 2
Ihsv = cv2.cvtColor(I, cv2.COLOR_BGR2HSV)
print("Muc sang trung binh cua kenh S:", np.mean(Ihsv[:, :, 1]))
# cv2.imshow("Ihsv", Ihsv[:, :, 0])

# 3
hist = cv2.calcHist(Ihsv[:, :, 2], channels=[2], mask=None, histSize=[256], ranges=[0, 256])
plt.plot(hist)
plt.title('Histogram cua kenh V')
# plt.show()


# 4
Is = cv2.blur(Ihsv[:, :, 1], (5, 5))
# cv2.imshow("lam tron", Is)

# 5
thresh, Ib = cv2.threshold(Is, 0, 255, cv2.THRESH_OTSU)
contours, con = cv2.findContours(Ib, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# cv2.drawContours(I, contours, -1, (0, 255, 0), 1)
# cv2.imshow("Contours", I)

max_tiso = 0.0
contours_max = []
for ct in contours:
    if cv2.contourArea(ct) > 0:
        if max_tiso <= (cv2.arcLength(ct, True) / cv2.contourArea(ct)):
            max_tiso = (cv2.arcLength(ct, True) / cv2.contourArea(ct))
            contours_max = ct

cv2.drawContours(I, [contours_max], -1, (0, 255, 0), 2)
cv2.imshow("contours ti so", I)

cv2.waitKey(0)