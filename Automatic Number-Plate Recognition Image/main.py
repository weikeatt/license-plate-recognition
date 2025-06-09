import cv2
import imutils
import numpy as np
import easyocr

reader = easyocr.Reader(['en', 'ch_sim'], gpu=False)

input_image = 'china.png'
#input_image = 'japan.png'
#input_image = 'korea.jpg'
#input_image = 'thai.jpg'

img = cv2.imread(input_image)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# cv2.imshow("Output", img)

bfilter = cv2.bilateralFilter(gray, 11, 17, 17)  # Clearer
edge = cv2.Canny(bfilter, 30, 200)   # Edge detection
# cv2.imshow("result", edge)

# Draw rectangle around car plate number
keypoints = cv2.findContours(edge.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
contours = imutils.grab_contours(keypoints)
contours = sorted(contours, key=cv2.contourArea, reverse=True)[:10]

location = None
for contour in contours:
    approx = cv2.approxPolyDP(contour, 10, True)
    if len(approx) == 4:
        location = approx
        #print(location)
        break

# Focus on ROI and crop
mask = np.zeros(gray.shape, np.uint8)
new_image = cv2.drawContours(mask, [location], 0, 255, -1)
new_image = cv2.bitwise_and(img, img, mask=mask)
cv2.imshow("Output", new_image)

(x, y) = np.where(mask == 255)
(x1, y1) = (np.min(x), np.min(y))
(x2, y2) = (np.max(x), np.max(y))
cropped_image = gray[x1:x2+10, y1:y2+10]
# cv2.imshow("hey", cropped_image)

result = reader.readtext(cropped_image, detail=0)
print(result)


cv2.waitKey(0)

