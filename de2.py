import cv2
import numpy as np
from matplotlib import pyplot as plt

# 1. đọc ảnh
I = cv2.imread("./I04.jpg")
# cv2.imshow("I", I)

# 2. size ảnh về kích thước 256x256
I2 = cv2.resize(I, (256, 256))
# cv2.imshow("I2", I2)

# 3. chuyển ảnh sang HSV
Ihsv = cv2.cvtColor(I, cv2.COLOR_BGR2HSV)
# cv2.imshow("kenh S", Ihsv[:, :, 1])

# 4. làm trơn kênh V của ảnh Ihsv
Ihsv_tron = cv2.blur(Ihsv[:, :, 2], (3, 3))
# cv2.imshow("Ihsv_tron", Ihsv_tron)

I3 = cv2.cvtColor(Ihsv, cv2.COLOR_HSV2BGR)
# cv2.imshow("I3", I3)

# 5. xác định biên theo phương pháp Candy của kênh
Ivb = cv2.Canny(Ihsv[:, :, 2], 0, 255)
# cv2.imshow("Ivb", Ivb)

# 6. xác định histogram của kênh S của ảnh Ihsv. vẽ histogram

# xây dựng hàm tính histogram
def tinh_his(Ihsv):
    r = Ihsv.shape[0]
    c = Ihsv.shape[1]
    mat_his = np.zeros(256, dtype='uint32')
    for i in range(0, r):
        for j in range(0, c):
            mat = Ihsv[i][j]
            mat_his[mat] = mat_his[mat] + 1
    return mat_his


hist = tinh_his(Ihsv[:, :, 1])
# cv2.imshow("Ihsv kenh S", Ihsv[:, :, 1])
# print(hist)
# plt.plot(hist)
# plt.show()

# xử dụng hàm opencv
hist_function = cv2.calcHist(Ihsv[:, :, 1], channels=[2], mask=None, histSize=[256], ranges=[0, 256])
plt.plot(hist_function)
# print(hist_function)
# plt.show()

# ----------- cân bằng histogram -------------
hist_canbang = cv2.equalizeHist(Ihsv[:, :, 1])
# cv2.imshow("hist can bang", Ihsv[:, :, 1])
plt.plot(hist_canbang)
# plt.show()

cv2.waitKey(0)
