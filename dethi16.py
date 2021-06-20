import numpy as np
import cv2

# 1
I = cv2.imread("./anhthi/anh5.jpg")
print("Ti le do cao va do rong :", I.shape[0]/I.shape[1])
# cv2.imshow("I", I)

# 2
Ihsv = cv2.cvtColor(I, cv2.COLOR_BGR2HSV)
print("mức sáng trung bình của kênh S", np.mean(Ihsv[:, :, 1]))
# cv2.imshow("Ihsv kenh H", Ihsv[:, :, 2])

# 3
Is = cv2.medianBlur(Ihsv[:, :, 1], 5)
# cv2.imshow("Is",Is)

# 4
thresh, Ib = cv2.threshold(255-Is, 0, 255, cv2.THRESH_OTSU)
# cv2.imshow("Ib", Ib)

contours, con = cv2.findContours(Ib, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

cv_max = 0.0
contours_max = []
for ct in contours:
    if cv_max <= cv2.arcLength(ct, True):
        cv_max = cv2.arcLength(ct, True)
        contours_max = ct
cv2.drawContours(I, [contours_max], -1, (0, 0, 255), 3)
# cv2.imshow("Contours I",I)

# 5


def gianmucxam(Igray):
    max_Igray = np.max(Igray)
    min_Igray = np.min(Igray)

    I_gray = np.zeros(256, dtype='uint8')
    # giãn mức maxxxx
    for i in range(0, 256):
        I_gray[i] = (255 * (i - min_Igray)) // (max_Igray - min_Igray)
    for u in range(0, Igray.shape[0]):
        for v in range(0, Igray.shape[1]):
            Igray[u][v] = I_gray[Igray[u][v]]
    return Igray


Ihsv[:, :, 2] = gianmucxam(Ihsv[:, :, 2])
# cv2.imshow("gian muc xam kenh V", Ihsv[:, :, 2])
I = cv2.cvtColor(Ihsv, cv2.COLOR_HSV2RGB)
cv2.imshow("bien doi Ihsv ve RGB", I)
cv2.waitKey(0)