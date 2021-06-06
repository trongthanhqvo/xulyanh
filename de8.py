import cv2
import numpy as np

# 1.
I = cv2.imread("./anhthi/anh5.jpg")
# cv2.imshow("I", I)

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
contours, con = cv2.findContours(Ib, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# cv2.drawContours(I, contours, -1, (255, 0, 0), 3)  # blue
# cv2.imshow("Contours Ib", I)

#   contours co chu vi lon nhat
max_cv = 0.0
contours_max_cv = []
for ct in contours:
    if max_cv <= cv2.arcLength(ct, True):
        max_cv = cv2.arcLength(ct, True)
        contours_max_cv = ct
# cv2.drawContours(I, [contours_max_cv], -1, (0, 0, 255), 3)  # red
# cv2.imshow("Contours CV max", I)
#   contours co dien tich lon nhat
max_s = 0.0
contours_max_s = []

for ct in contours:
    if max_s <= cv2.contourArea(ct):
        max_s = cv2.contourArea(ct)
        contours_max_s = ct
# cv2.drawContours(I, [contours_max_s], -1, (0, 255, 0), 3)  # green
# cv2.imshow("Contours dien tich max", I)


# Giãn mức xám của kênh V của ảnh Ihsv lên khoảng tối đa [0,255] được ảnh Iv2.
# Hiển thị ảnh Iv2.


def gianmucxam(Ig):
    max_Ig = np.max(Ig)
    min_Ig = np.min(Ig)
    I_gray = np.zeros(256, dtype='uint8')
    for i in range(0, 256):
        I_gray[i] = (255 * (i - min_Ig)) // (max_Ig - min_Ig)
    for u in range(0, Ig.shape[0]):
        for v in range(0, Ig.shape[1]):
            Ig[u][v] = I_gray[Ig[u][v]]
    return Ig


Ihsv[:, :, 2] = gianmucxam(Ihsv[:, :, 2])
I = cv2.cvtColor(Ihsv, cv2.COLOR_HSV2BGR)
cv2.imshow("Gian muc xam", I)

cv2.waitKey()