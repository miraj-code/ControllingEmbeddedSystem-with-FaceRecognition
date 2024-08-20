import cv2
from deepface import DeepFace
import RPi.GPIO as GPIO
import time

# GPIO Setup
LED_PIN = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)

# Initialize camera
camera = cv2.VideoCapture(0)

try:
    while True:
        ret, frame = camera.read()
        if not ret:
            break
        
        # Perform face recognition
        result = DeepFace.analyze(frame, actions=['emotion'], enforce_detection=False)
        if result:
            GPIO.output(LED_PIN, GPIO.HIGH)  # Turn LED on
        else:
            GPIO.output(LED_PIN, GPIO.LOW)  # Turn LED off
        
        # Display frame (optional)
        cv2.imshow("Camera", frame)
        
        # Exit on pressing 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

except KeyboardInterrupt:
    pass

finally:
    camera.release()
    cv2.destroyAllWindows()
    GPIO.cleanup()  # Reset GPIO settings

)