import cv2
import numpy as np

# 1:đọc ảnh anh5.jpg bằng ma trận I.hiển thị ảnh
I = cv2.imread("./anhthi/anh5.jpg")
# cv2.imshow("anh I",I)

# 2 :Chuyển ảnh I sang ảnh grayscale theo công thức biến đổi bộ mầu (r,g,b) về mức xám=0.39*r+0.50*g+0.11*b, được ảnh Ig. Hiển thị ảnh Ig.'''
Ig = np.zeros((I.shape[0], I.shape[1]), dtype="uint8")
for i in range(0, Ig.shape[0]):
    for j in range(0, Ig.shape[1]):
        Ig[i][j] = int(0.39 * I[i][j][2] + 0.5 * I[i][j][1] + 0.11 * I[i][j][0])
# cv2.imshow("Ig convert", Ig)

# 3
# 3.1lấy biên của ảnh Ig bằng Candy thành ảnh biên Ie nhịp phân.
Ie = cv2.Canny(Ig, 0, 255)
# cv2.imshow("Ie", Ie)
# 3.2 Kiểm tra pixel có tọa độ dòng y=160, cột x=326 có là điểm biên của ảnh Ig theo phép dò biên Canny không
y = 160
x = 326
if Ie[y][x] == 255:
    print("là điểm biên của phép dò biên Canny")
else:
    print("không là điểm biên của phép dò biên Canny")

# 4 Nhị phân hóa anh Ig theo ngưỡng otsu dc ảnh ib.hiển thi Ib.
thresh, Ib = cv2.threshold(Ig, 0, 255, cv2.THRESH_OTSU)
# cv2.imshow('Anh nhi phan Ib', Ib)

# 5
# 5.1 Tìm các contour của ảnh Ib.
contours, con = cv2.findContours(Ib, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

max_cv = 0.0
contours_max = []
for ct in contours:
    if max_cv <= cv2.arcLength(ct, True):
        max_cv = cv2.arcLength(ct, True)
        contours_max = ct
cv2.drawContours(I, [contours_max], -1, (0, 255, 255), 2)
cv2.imshow("Anh sau khi ve lan 2", I)

cv2.waitKey(0)