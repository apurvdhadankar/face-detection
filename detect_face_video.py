import cv2

# Load the cascade
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# To capture video from webcam. 
cap = cv2.VideoCapture(0)
# To use a video file as input 
# cap = cv2.VideoCapture('filename.mp4')
while True:

    status, photo = cap.read()

     # Convert to grayscale
    gray = cv2.cvtColor(photo, cv2.COLOR_BGR2GRAY)

    # Detect the faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    # Draw the rectangle around each face
    for (x, y, w, h) in faces:
        cv2.rectangle(photo, (x, y), (x+w, y+h), (255, 0, 0), 2)


    cv2.putText(photo, "Hey What's up", (250, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (0,255,0), 2)
    cv2.imshow('hi', photo)
    
    if cv2.waitKey(1) == 13:  #press Enter key to close
        break

cv2.destroyAllWindows()
cap.release()