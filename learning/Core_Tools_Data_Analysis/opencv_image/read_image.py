import cv2 

img = cv2.imread('images/1.jpg')
if img is None:
    print("Error: Could not read the image.")
else:
    cv2.imshow('Image', img) 
    cv2.waitKey(0)  
    cv2.destroyAllWindows()