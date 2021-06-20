import cv2
import numpy as np

# 1
I = cv2.imread("./anhthi/anh5.jpg")
# cv2.imshow("I", I)

# 2
Ihsv = cv2.cvtColor(I, cv2.COLOR_BGR2HSV)
print("Muc sang lon nhat cua kenh V:", np.max(Ihsv[:, :, 2]))
# cv2.imshow("Ihsv kenh S", Ihsv[:, :, 1])

# 3
Iv = cv2.blur(Ihsv[:, :, 2], (3, 3))
# cv2.imshow('Lam tron kenh V', Iv)

# 5
thresh, Ib = cv2.threshold(Iv, 0, 255, cv2.THRESH_OTSU)
contours, con = cv2.findContours(Ib, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

max_cv = 0.0
contours_max = []
for ct in contours:
    if max_cv <= cv2.arcLength(ct, True):
        max_cv = cv2.arcLength(ct, True)
        contours_max = ct
print("chu vi co lon nhat:", max_cv)
cv2.drawContours(I, [contours_max], -1, (0, 0, 255), 2)  # red
# cv2.imshow("Contours", I)

# 6
Ihsv_canbang = cv2.equalizeHist(Ihsv[:, :, 2])
# cv2.imshow("Anh can bang histogram", Ihsv_canbang)
I = cv2.cvtColor(Ihsv, cv2.COLOR_HSV2BGR)
# cv2.imshow("I convert", I)
cv2.waitKey(0)