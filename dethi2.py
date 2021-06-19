import cv2
import numpy as np
from matplotlib import pyplot as plt

# 1
I = cv2.imread("./anhthi/I04.jpg")
# cv2.imshow("I", I)

# 2
print("ti le giua do rong va do cao  cua anh I:", I.shape[0]/I.shape[1])

# 3
I2 = cv2.resize(I, (256, 256))
# cv2.imshow("I2", I2)

# 4
Ihsv = cv2.cvtColor(I, cv2.COLOR_BGR2HSV)
# cv2.imshow("Ihsv kenh s", Ihsv[:, :, 1])

# 5
Ivb = cv2.Canny(Ihsv[:, :, 2], 0, 255)
cv2.imshow("Bien thuat toan canny", Ihsv)

# 6

# viết hàm để tính histogram
def tinh_his(Igray):
    r = Igray.shape[0]
    c = Igray.shape[1]
    mang_his = np.zeros(256, dtype='uint32')
    for i in range(0, r):
        for j in range(0, c):
            g = Igray[i][j]
            mang_his[g] = mang_his[g] + 1
    return mang_his

hist = tinh_his(Ihsv[:, :, 1])
# plt.plot(hist)
# plt.show()

# sử dụng hàm của opencv
hist_function = cv2.calcHist(Ihsv[:, :, 1], channels=[2], mask=None, histSize=[256], ranges=[0, 256])
plt.plot(hist_function)
plt.show()

cv2.waitKey(0)