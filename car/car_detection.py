import cv2

# Capture frames from video
cap = cv2.VideoCapture('video.avi')

# Trained  XML classifiers describes some featurs of some object we want to detect
car_cascade = cv2.CascadeClassifier('cars.xml')

# loops runs if capturing has been initialized
while True:
    # reads frames from a video
    ret, frames = cap.read()

    # convert to gray scale to each frames
    gray = cv2.cvtColor(frames, cv2.COLOR_BGR2GRAY)

    # Detects cars of different sizes in the input image
    cars = car_cascade.detectMultiScale(gray, 1.1, 1)

    # To draw rectangles in each car
    for (x,y,w,h) in cars:
        cv2.rectangle(frames,(x,y),(x+w,y+h),(0,0,255),2)

    # Display frames in a window
    cv2.imshow('video2', frames)

    # wait for Enter key to stop
    if cv2.waitKey(33) == 13:
        break


# Deallocate any associated memory usage
cv2.destroyAllWindows() 


