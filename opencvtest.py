import sys
import cv2

img = cv2.imread(sys.argv[1],0)
img = cv2.resize(img, (640, 480))
cv2.imshow('OpenCV TEST' , img)

cv2.waitKey(0)
cv2.destroyAllWindows()
