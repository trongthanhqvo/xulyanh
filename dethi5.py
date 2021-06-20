import cv2
import numpy as np
from matplotlib import pyplot as plt

# 1
I = cv2.imread("./anhthi/Coins.jpg")
# cv2.imshow("I", I)


# 2
Ig = np.zeros((I.shape[0], I.shape[1]), dtype='uint8')  # ảnh đen
for i in range(0, I.shape[0]):
    for j in range(0, I.shape[1]):
        Ig[i][j] = int(0.39 * I[i][j][2] + 0.5 * I[i][j][1] + 0.11 * I[i][j][0])

print("Muc xam lon nhat:", np.max(Ig))
# cv2.imshow("Ig convert", Ig)

    # cách 2: sử dụng hàm của opencv
# Ig_function = cv2.cvtColor(I, cv2.COLOR_BGR2GRAY)
# cv2.imshow('Ig funtion opencv', Ig_function)

# 3
# theo hướng X
Ig_gradientX = cv2.Sobel(Ig, cv2.CV_64F, 1, 0, 5, ksize=5)
plt.subplot(1, 2, 1)
plt.title("Ig_gradientX")
plt.imshow(Ig_gradientX, cmap='gray')


# theo hướng Y
Ig_gradientY = cv2.Sobel(Ig, cv2.CV_64F, 0, 1, 5, ksize=3)
plt.subplot(1, 2, 2)
plt.title("Ig_gradientY")
# plt.xticks([])
# plt.yticks([])
plt.imshow(Ig_gradientY, cmap='gray')
# plt.show()


# 4
Ie = cv2.Canny(Ig, 0, 255)

h = Ig.shape[0]
w = Ig.shape[1]
y = 179  # hàng
x = 123  # cột
#
print("Cac gia tri muc xam:")
for i in range(-1, 2):
    for j in range(-1, 2):
        #         y-i vs h (Ig.shape[0])               x-j vs w (Ig.shape[1])
        if ((y + i) >= 0) & ((y + i) <= h - 1) & ((x + j) >= 0) & ((x + j) <= w - 1):
            print("matrix[{}][{}]={}".format(i, j, Ig[y+i, x+j]))
        else:
            print("matrix[{}][{}]={}".format(i, j, "vuot qua"))
# cv2.imshow("Ie canny", Ie)

# 5
thresh, Ib = cv2.threshold(Ig, 0, 255, cv2.THRESH_OTSU)
# cv2.imshow("Ib", Ib)
contours, con = cv2.findContours(Ib, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(I, contours, -1, (255, 0, 0), 1)
cv2.imshow("I contours", I)
cv2.waitKey(0)
