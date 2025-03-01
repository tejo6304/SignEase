import cv2
import numpy as np
from tensorflow import keras
from cvzone.HandTrackingModule import HandDetector

# Load the trained model (make sure this path is correct for your environment)
model_path = 'C:/Users/saida/Downloads/signease/Model/keras_model.h5'
model = keras.models.load_model(model_path)

# Define the categories (replace with your actual categories)
categories = { 
    0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9',
    10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F', 16: 'G', 17: 'H', 18: 'I', 19: 'J',
    20: 'K', 21: 'L', 22: 'M', 23: 'N', 24: 'O', 25: 'P', 26: 'Q', 27: 'R', 28: 'S', 29: 'T',
    30: 'U', 31: 'V', 32: 'W', 33: 'X', 34: 'Y', 35: 'Z'
}

# Initialize the hand detector
detector = HandDetector(maxHands=1)  # Adjust maxHands based on your use case

# Initialize the camera
cap = cv2.VideoCapture(0)  # Use 0 for default camera

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Find hands in the frame
    hands, frame = detector.findHands(frame)

    if hands:
        hand = hands[0]
        x, y, w, h = hand['bbox']  # Get the bounding box of the hand

        # Crop the hand region and resize it to the model's input size (224x224)
        imgCrop = frame[y:y + h, x:x + w]
        imgResize = cv2.resize(imgCrop, (224, 224))  # Resize to 224x224 (model input size)
        imgResize = imgResize / 255.0  # Normalize pixel values
        imgResize = np.expand_dims(imgResize, axis=0)  # Add batch dimension

        # Make a prediction
        prediction = model.predict(imgResize)
        predicted_class = np.argmax(prediction)
        predicted_label = categories.get(predicted_class, 'Unknown')

        # Display the prediction on the frame
        cv2.putText(frame, f"Prediction: {predicted_label}", (x, y - 20), 
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # Show the frame with the hand and prediction
    cv2.imshow("Live Sign Language Recognition", frame)

    # Exit on pressing 'q'
    if cv2.waitKey(100) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
