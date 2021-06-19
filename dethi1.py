import cv2
import numpy
import numpy as np

# 1
I = cv2.imread("./anhthi/the_cancuoc_congdan.jpg")
# cv2.imshow("I", I[:, :, 0])


# 2
# xử dụng hàm của opencv
# Ig = cv2.cvtColor(I, cv2.COLOR_BGR2GRAY)
# cv2.imshow("Ig function opencv", Ig)

    # cách 2
Ig = np.zeros((I.shape[0], I.shape[1]), dtype="uint8")
for i in range(0, Ig.shape[0]):
    for j in range(0, Ig.shape[1]):
        Ig[i][j] = int(0.39 * I[i][j][2] + 0.5 * I[i][j][1] + 0.11 * I[i][j][0])
# cv2.imshow("Ig convert", Ig)


# 3
# 0 là màu đen, 255 là màu trắng
thresh, Ib = cv2.threshold(Ig, 0, 255, cv2.THRESH_OTSU)
# cv2.imshow("Ib", Ib)

# 4
Im = cv2.blur(Ig, (5, 5))
# cv2.imshow("Im", Im)

# 5
contours, con = cv2.findContours(Im, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

cv2.drawContours(I, contours, -1, (255, 0, 0), 3)
cv2.imshow("Contours I", I)

cv2.waitKey(0)

