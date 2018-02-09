import sys

import numpy as np
import cv2
import time

starttime = time.time()

img = cv2.imread(sys.argv[1])
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


img = cv2.adaptiveThreshold(img,255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11 ,2)
ret,gray = cv2.threshold(img,96,255,cv2.THRESH_BINARY)

gray = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY )[1]
label = cv2.connectedComponentsWithStats(gray)

n = label[0] - 1
cog = np.delete(label[3], 0, 0)


for i in range(n):
    img = cv2.circle(img,(int(cog[i][0]),int(cog[i][1])), 10, (0,255,0), -1)
#    print("x=",int(cog[i][0]), "y=", int(cog[i][1]))


#img = cv2.resize(img, (640, 480))
cv2.imwrite('output.jpg' , img)
cv2.imwrite('op_gry.jpg' , gray)

endtime = time.time()
interval = endtime - starttime
print("start time = " + str(starttime))
print("  end time = " + str(endtime))
print(str(interval) + "sec")

print("Prg OK")

cv2.waitKey(0)
cv2.destroyAllWindows()
