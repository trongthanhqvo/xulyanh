import cv2
import numpy as np


I = cv2.imread("./anhthi/I04.jpg")
# cv2.imshow("I", I)

# 1
kt = I.shape[0]/I.shape[1]
print("Ti le do cao va do rong cua anh:", kt)

# 2
I2 = cv2.resize(I, (256, int(256*kt)))
print("Ti le do cao va do rong cua anh I2:", I2.shape[0]/I2.shape[1])
# cv2.imshow("I2 resize", I2)

# 3
Ihsv = cv2.cvtColor(I, cv2.COLOR_BGR2HSV)
# cv2.imshow("Ihsv", Ihsv[:, :, 1])

# 4
Ihsv[:, :, 1] = cv2.medianBlur(Ihsv[:, :, 1], 9)
# cv2.imshow("Ihsv tron", Ihsv[:, :, 1])
I3 = cv2.cvtColor(Ihsv, cv2.COLOR_HSV2RGB)
# cv2.imshow("I3", I3)

# 5
Ihsv[:, :, 1] = cv2.equalizeHist(Ihsv[:, :, 1])
# cv2.imshow("can bang", Ihsv[:, :, 1])
I4 = cv2.cvtColor(Ihsv, cv2.COLOR_HSV2RGB)
cv2.imshow("I4", I4)
cv2.waitKey(0)