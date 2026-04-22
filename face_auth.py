import cv2

def authenticate():
    face_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
    )

    cam = cv2.VideoCapture(0)
    print("🔍 Looking for your face...")

    while True:
        ret, frame = cam.read()

        if not ret:
            print("❌ Camera error")
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        # Draw rectangle on face
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

        cv2.imshow("Face Authentication", frame)

        # If face detected → allow access
        if len(faces) > 0:
            print("✅ Face Detected - Access Granted")
            cam.release()
            cv2.destroyAllWindows()
            return True

        # Press Q to quit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cam.release()
    cv2.destroyAllWindows()
    return False
