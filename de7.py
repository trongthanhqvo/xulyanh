import cv2
import numpy as np
from matplotlib import pyplot as plt
from copy import deepcopy

# 1
I = cv2.imread("./anhthi/Coins.jpg")
# cv2.imshow("Image", I)

# 2. chuyển ảnh qua gray
Ig = np.zeros((I.shape[0], I.shape[1]), dtype='uint8')
for i in range(0, I.shape[0]):
    for j in range(0, I.shape[1]):
        Ig[i][j] = int(0.39 * I[i][j][2] + 0.5 * I[i][j][1] + 0.11 * I[i][j][0])

print("muc xam lon nhat:", np.max(Ig))
# cv2.imshow("Image gray", Ig)

# 3. xác định ma trận gradient của ảnh Ig theo hướng x và theo hướng y. Hiển thị
# theo huong X
Ig_gradientX = cv2.Sobel(Ig, cv2.CV_64F, 0, 1, 3, ksize=5)
plt.subplot(3, 3, 1)
plt.imshow(Ig_gradientX, cmap="gray")
plt.title("Ig_gradientX")
plt.xticks([])
plt.yticks([])

# theo huong Y
Ig_gradientY = cv2.Sobel(Ig, cv2.CV_64F, 0, 1, 3, ksize=5)
plt.subplot(3, 3, 2)
plt.imshow(Ig_gradientY, cmap="gray")
plt.title("Ig_gradientY")
plt.xticks([])
plt.yticks([])


# Xác định ma trận gradient của ảnh Ig theo cả 2 hướng y và hướng x
# với phương pháp Sobel được ảnh Igradient=(IgradientX+IgradientY)//2. Hiển thi Igradient.
Ig_gradientXY = (Ig_gradientX + Ig_gradientY) // 2
plt.subplot(3, 3, 3)
plt.imshow(Ig_gradientXY, cmap="gray")
plt.title("Ig_gradientXY")
plt.xticks([])
plt.yticks([])
# plt.show()

# 4. Lấy biên bằng phương pháp Candy
#     Kiểm tra pixel có tọa độ dòng y=181, cột x=120 có là điểm biên của ảnh Ig theo phép dò biên Canny không?
Ie = cv2.Canny(Ig, 0, 255)
y = 181
x = 120
try:
    if Ie[y][x] == 255:
        print("La diem bien cua anh Ig")
    else:
        print("Khong phai la diem bien cua anh Ig")
except:
    print("Vuot qua so pic")
# cv2.imshow("Lay bien bang pp candy", Ie)

                    # ---------------LAM THEM---------------------
    # Xác định biên bằng ma trân gradientXY bằng pp dò biên Soble và ngưỡng  cho trước (nguong=50)
# Ig_gradientX = cv2.Sobel(Ig, cv2.CV_64F, 0, 1, 3, ksize=5)
# Ig_gradientY = cv2.Sobel(Ig, cv2.CV_64F, 0, 1, 3, ksize=5)
# Ig_gradientXY = (Ig_gradientX + Ig_gradientY) // 2
nguong = 50
Ig1 = deepcopy(Ig_gradientXY)
Ie2 = np.zeros((Ig1.shape[0], Ig1.shape[1]), dtype='uint8')
for i in range(0, Ig1.shape[0]):
    for j in range(0, Ig1.shape[1]):
        if Ig1[i][j] >= nguong:
            Ie2[i][j] = 255
        else:
            Ie2[i][j] = 0
# cv2.imshow("Lay bien bang pp Soble va ma tran gradientXY", Ie2)


# 5. Hiển thi các giá trị mức xám của ảnh Ig trong lân cận cửa sổ
# 3x3 của pixel có tọa độ dòng y=181, cột x=120.
h = Ig.shape[0]
w = Ig.shape[1]
y = 181
x = 120
print("Cac gia tri muc xam:")
for i in range(0, 3):
    for j in range(0, 3):
        #         y-i vs h (Ig.shape[0])               x-j vs w (Ig.shape[1])
        if ((y + i) >= 0) & ((y + i) <= h - 1) & ((x + j) >= 0) & ((x + j) <= w - 1):
            print("matrix[{}][{}]={}".format(i, j, Ig[y+i, x+j]))
        else:
            print("matrix[{}][{}]={}".format(i, j, "vuot qua"))

# 6. Nhi phân ảnh theo ngưỡng Otsu được ảnh nền đen Ib
thresh, Ib = cv2.threshold(Ig, 0, 255, cv2.THRESH_OTSU)
# cv2.imshow("Image binary", Ib)
contours, con = cv2.findContours(Ib, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(I, contours, -1, (0, 0, 255), 2)  # blue
cv2.imshow("Contour Image", I)

cv2.waitKey()

