import cv2

img = cv2.imread('images/1.jpg')
blurred = cv2.GaussianBlur(img, (3, 3), 0) # Apply Gaussian blur to the image with a kernel size of 3x3
# gaussian blur is used to reduce noise and detail in the image
#3x3, 5x5, 7x7, 15x15 are common kernel sizes

edges = cv2.Canny(img, 100, 200) # Apply Canny edge detection with thresholds 100 and 200
# 100 and 200 are the lower and upper thresholds for edge detection