import cv2
import numpy as np

kernel = np.asarray([[0, -1, 0], [-1, 5, -1], [0, -1, 0]], np.float32)

img = cv2.imread("shrek.jpg")
mask = cv2.filter2D(img, -1, kernel)

cv2.imshow("image", mask)
cv2.waitKey(0)
cv2.destroyAllWindows()

blendDim = (200, 200)
blendOne = cv2.resize(cv2.imread("farquaad.jpg"), blendDim)
blendTwo = cv2.resize(cv2.imread("markiplier.jpg"), blendDim)
result = cv2.imread("shrek.jpg")

result = cv2.addWeighted(blendOne, 0.7, blendTwo, 0.3, 0.0, result)
cv2.imshow("marquaad", result)
cv2.waitKey(0)
cv2.destroyAllWindows()

print(img)