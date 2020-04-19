import cv2

# Load the cascade
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)


status, photo = cap.read()

cv2.imwrite('myimg.png', photo)
cap.release()

# Read the input image
photo = cv2.imread('myimg.png')

# Convert into grayscale
gray = cv2.cvtColor(photo, cv2.COLOR_BGR2GRAY)

# Detect faces
faces = face_cascade.detectMultiScale(gray, 1.1, 4)

# Draw rectangle around the faces
for (x, y, w, h) in faces:
    cv2.rectangle(photo, (x, y), (x + w, y + h), (255, 0, 0), 2)

# Display the output
#photo[200:300]=[0,255,0]    # to change color of photo in rowise
cv2.imshow('my image', photo)
cv2.waitKey(5000)
        
cv2.destroyAllWindows()

