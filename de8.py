import cv2
import numpy as np

# 1.
I = cv2.imread("./anhthi/contour1.jpg")
cv2.imshow("I", I)

# 2. chuyển ảnh  sang HSV, hiển thị mức sáng lớn nhất của kênh V
Ihsv = cv2.cvtColor(I, cv2.COLOR_BGR2HSV)
print("muc sang lon nhat cua kenh V:", np.max(Ihsv[:, :, 2]))
# cv2.imshow("Kenh V", Ihsv[:, :, 2])


# 3. Làm trơn ảnh kênh S của Ihsv theo bộ lọc trung bình, ích thước của sổ lân cận là 5x5
Is = cv2.blur(Ihsv[:, :, 1], (5, 5))
# cv2.imshow("Lam tron kenh S ", Is)


# 4. Nhị phân hóa ảnh nghịch đảo Is (ảnh 255-Is, trắng -> đen; đen->trắng)
#    theo ngưỡng Otsu được ảnh nhị phân Ib. Hiển thị ảnh Ib.
thresh, Ib = cv2.threshold(255-Is, 0, 255, cv2.THRESH_OTSU)
# cv2.imshow("Ib", Ib)

# 5. Xác định các contours, vẽ lên ảnh gốc
contours, con = cv2.findContours(Ib, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(I, contours, -1, (0, 0, 255), 2)  # red
# cv2.imshow("Contours Ib", I)

#     Xác định contours có diện tích lớn nhất
max_s = 0.0
contours_max = []
for ct in contours:
    if max_s <= cv2.contourArea(ct):
        max_s = cv2.contourArea(ct)
        contours_max = ct
print("Dien tich lon nhat:", max_s)
cv2.drawContours(I, [contours_max], -1, (0, 255, 0), 2)  # green
# cv2.imshow("Contours S max", I)

#     Xác định contours có chu vi lớn nhất
max_cv = 0.0
contours_max_cv = []
for ct in contours:
    if max_cv <= cv2.arcLength(ct, True):
        max_cv = cv2.arcLength(ct, True)
        contours_max_cv = ct
print("Chu vi lon nhat:", max_cv)
cv2.drawContours(I, [contours_max_cv], -1, (255, 0, 0), 3)  # blue
cv2.imshow("Contours CV max", I)

cv2.waitKey()