import cv2
import numpy as np

I = cv2.imread("./I04.jpg",1)
#cv2.imshow("kenh B",I[:, :, 0])
#cv2.imshow("kenh G",I[:, :, 1])
#cv2.imshow("kenh R",I[:,:,2])

Ig = cv2.cvtColor(I, cv2.COLOR_BGR2GRAY)
#cv2.imshow("gray",Ig)

Ig = np.zeros((I.shape[0], I.shape[1]), dtype='uint8')
# cv2.imshow("Ig",Ig)
for i in range(0, I.shape[0]):
    for j in range(0, I.shape[1]):
        d = 10 * int(I[i][j][2]) + 50 * int(I[i][j][1]) + 11 * int(I[i][j][0])
        d = d // 100
        Ig[i][j] = d

cv2.imshow("Ig gray", Ig)

print("do cao:", Ig.shape[0])
print("do rong:", Ig.shape[1])

Ig_hsv = cv2.cvtColor(I, cv2.COLOR_BGR2HSV)
# cv2.imshow("goc",I)

# độ sáng max, min, trung bình của kệnh V
print("max:", np.max(Ig_hsv[:, :, 1]))
print("min:", np.min(Ig_hsv[:, :, 1]))
print("trung binh:", np.mean(Ig_hsv[:, :, 1]))

cv2.imshow("Ig_HSV", Ig_hsv[:, :, 2])
cv2.waitKey()
