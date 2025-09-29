import cv2
import imutils
import datetime
import time

# Initialize camera
camera = cv2.VideoCapture(0)  # 0 for Pi Camera or USB webcam
time.sleep(2)  # Allow camera to warm up

first_frame = None

while True:
    # Read frame
    ret, frame = camera.read()
    if not ret:
        break

    # Resize frame for faster processing
    frame = imutils.resize(frame, width=500)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (21, 21), 0)

    # Initialize first frame
    if first_frame is None:
        first_frame = gray
        continue

    # Compute difference between first frame and current frame
    frame_delta = cv2.absdiff(first_frame, gray)
    thresh = cv2.threshold(frame_delta, 25, 255, cv2.THRESH_BINARY)[1]
    thresh = cv2.dilate(thresh, None, iterations=2)

    # Find contours (i.e., moving objects)
    contours, _ = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        if cv2.contourArea(contour) < 1000:  # Ignore small movements
            continue
        # Draw rectangle around motion
        (x, y, w, h) = cv2.boundingRect(contour)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Save image with timestamp
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        cv2.imwrite(f"visitor_{timestamp}.jpg", frame)
        print(f"[INFO] Visitor detected! Image saved as visitor_{timestamp}.jpg")

    # Display frame (optional)
    cv2.imshow("Visitor Monitor", frame)

    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):  # Press 'q' to quit
        break

# Cleanup
camera.release()
cv2.destroyAllWindows()

python3 visitor_monitor.py
