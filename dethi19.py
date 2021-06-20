import cv2
import numpy as np
import matplotlib.pyplot as plt

#
I = cv2.imread("./anhthi/apple.jpg")
# cv2.imshow("I", I[:, :, 2])

# 2: ảnh xám
Ig = np.zeros((I.shape[0], I.shape[1]), dtype="uint8")#
for i in range(0, Ig.shape[0]):
    for j in range(0, Ig.shape[1]):
        Ig[i][j] = int(0.39 * I[i][j][2] + 0.5 * I[i][j][1] + 0.11 * I[i][j][0])
print("Múc xám trung bình :", np.mean(Ig))
# cv2.imshow("Ig convert", Ig)


# 3  Xác định ma trận gradient theo hướng x của ảnh Ig với phương pháp Sobel.Hiển thị 2 ma trận
# 3.1 hướng x Sobel:xác định biên
# theo hướng X
Ig_gradientX = cv2.Sobel(Ig, cv2.CV_64F, 1, 0, 5, ksize=5)
plt.subplot(1, 1, 1)
plt.title("Ig_gradientX")
plt.imshow(Ig_gradientX, cmap='gray')
# plt.show()

# 4
# 4.1 lấy biên của ảnh Ig bằng Candy thành ảnh biên Ie nhịp phân.: phương pháp dò biên
Ie = cv2.Canny(Ig, 0, 255)
# cv2.imshow("Ie", Ie)
# 4.2 Kiểm tra pixel có tọa độ dòng y=100, cột x=120 có là điểm biên của ảnh Ig theo phép dò biên Canny không
y = 100
x = 120
if Ie[y][x] == 255:
    print("là điểm biên của phép dò biên Canny")
else:
    print("không là điểm biên của phép dò biên Canny")

# 5
thresh, Ib = cv2.threshold(Ig, 0, 255, cv2.THRESH_OTSU)
cv2.imshow("Ib", Ib)
contours, con = cv2.findContours(Ib, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(I, contours, -1, (0, 255, 0), 2)
cv2.imshow('Cac duong contour tren anh goc', I)

max_s = 0.0
contours_max_s = []
for ct in contours:
    if max_s <= cv2.contourArea(ct):
        max_s = cv2.contourArea(ct)
        contours_max_s = ct
# cv2.drawContours(I, [contours_max_s], -1, (0, 255, 0), 2)  # green
# cv2.imshow("Contours dien tich max", I)
cv2.waitKey(0)

