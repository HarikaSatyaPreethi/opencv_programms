import cv2

img = cv2.imread("/home/preethi/Downloads/flower.jpg")
cv2.imshow("Flower", img)
cv2.waitKey(0)
cv2.destroyAllWindows()