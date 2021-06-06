import cv2
from matplotlib import pyplot as plt
import numpy as np


def tinh_his(Igray):
    r = Igray.shape[0]
    c = Igray.shape[1]

    mang_his = np.zeros(256, dtype='uint32')
    for i in range(0, r):
        for j in range(0, c):
            g = Igray[i][j]
            mang_his[g] = mang_his[g] + 1

    return mang_his


Igray = cv2.imread("I04.jpg")
# hist = tinh_his(Igray)
# cv2.imshow("Igray", Igray)
# plt.plot(hist)
# plt.show()

# Cân bằng histogram của ảnh
# hist_eq = cv2.equalizeHist(Igray)
# cv2.imshow("Anh can bang",hist_eq)
# plt.plot(hist_eq)
# plt.show()

# xác định histogram của kênh S
Ihsv = cv2.cvtColor(Igray, cv2.COLOR_RGB2HSV)
cv2.imshow("Ihsv", Ihsv)
hist = tinh_his(Ihsv[:, :, 0])
plt.plot(hist)
# plt.show()
# cân bằng histogram của kênh S
Ihsv_canbang = cv2.equalizeHist(Ihsv[:, :, 0])
print(Ihsv.shape)
cv2.imshow("Anh can bang histogram:", Ihsv_canbang)
plt.plot(Ihsv_canbang)
plt.show()

cv2.waitKey()






#Xác định histogram của kênh S của ảnh Ihsv
hist = cv2.calcHist(Ihsv[:, :, 1], channels=[2],mask=None,histSize=[256],ranges=[0,256])
plt.plot(hist)
plt.title('Histogram của kênh anh S của ảnh Ihsv')
plt.show()

I_tron = cv2.blur(Ihsv[:, :, 2], (3,3))
cv2.imshow('tron', I_tron)
I3 = cv2.cvtColor(Ihsv, cv2.COLOR_HSV2BGR)
cv2.imshow('I3', I3)


Ivb = cv2.Canny(Ihsv[:, :, 2], 0, 255)
cv2.imshow('canny', Ivb)

cv2.waitKey(0)

