import cv2
import numpy as np
import matplotlib.pyplot as plt

# 1
I = cv2.imread("./anhthi/hat1.PNG")
# cv2.imshow("anh I", I)

# 2:Chuyen anh sang bieu dien HSV được matran Ihsv . Hien thi kenh H. Xác định múc sáng max của kênh S
Ihsv = cv2.cvtColor(I, cv2.COLOR_BGR2HSV)
print("Muc xam lon nhat kenh S:", np.max(Ihsv[:, :, 1]))
# cv2.imshow("Kenh H", Ihsv[:, :, 0])


# 3:Xác định histogram của kênh V của Ihsv

hist = cv2.calcHist(Ihsv[:, :, 2], channels=[2], mask=None,histSize=[256], ranges=[0, 256])
plt.plot(hist)
plt.title('Histogram của kênh anh S của ảnh Ihsv')
# plt.show()


# 4:Làm trơn ảnh kênh S của Ihsv theo bộ lọc median, kích thước cửa sổ lân cận là 5x5 được ảnh Is. Hiển thị ảnh Is
Is = cv2.medianBlur(Ihsv[:, :, 1], 5)
# cv2.imshow("Is_medianblur", Is)

# 5
thresh, Ib = cv2.threshold(Is, 0, 255, cv2.THRESH_OTSU)
cv2.imshow('Anh nhi phan Ib', Ib)

# 5.2 Tìm các contour của ảnh Ib.
contours, con = cv2.findContours(Ib, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# cv2.drawContours(I, contours, -1, (0, 255, 0), 2) #mã màu xanh
# cv2.imshow('Cac duong contour tren anh goc', I)

# 5.3 Vẽ đường contour có chu vi  lớn nhất ở câu trên ảnh gốc I. Hiển thị ảnh I.
max_cv = 0.0
contours_max = []
for contour in contours:
    if max_cv <= cv2.arcLength(contour, True):
        max_cv = cv2.arcLength(contour, True)
        contours_max = contour
cv2.drawContours(I, [contours_max], -1, (0, 255, 0), 2)
# cv2.imshow("Anh sau khi ve lan 2", I)

cv2.waitKey(0)
