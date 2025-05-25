import cv2

img = cv2.imread('images/1.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # Convert to grayscale
img_resized = cv2.resize(gray, (0, 0), fx=0.1, fy=0.1) # Resize the image by 10% in both dimensions
resized = cv2.resize(img, (300, 300)) # Resize the image to 300x300 pixels
crop = img[50:200, 100:300]  # [y1:y2, x1:x2] # Crop the image from y=50 to y=200 and x=100 to x=300
cv2.imwrite('images/2.jpg', crop) # Save the cropped image
cv2.circle(img, (1250, 1250), 520, (0, 0, 255), -1)  # Draw a filled circle at (1250, 1250) with radius 520 and color red
cv2.line(img, (110, 110), (3000, 3000), (255, 0, 0), 3)  # Draw a blue line from (110, 110) to (3000, 3000) with thickness 3
cv2.rectangle(img, (50, 50), (2550, 2550), (0, 255, 0), 24)  # Draw a green rectangle from (50, 50) to (2550, 2550) with thickness 24