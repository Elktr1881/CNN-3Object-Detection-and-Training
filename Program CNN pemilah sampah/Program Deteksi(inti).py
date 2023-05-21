import cv2
import tensorflow as tf
import numpy as np

# Load model
model = tf.keras.models.load_model('D:\Project-project\Pemilah Sampah\Datasheet created\datasheet_new.h5')

# Define class labels
class_labels = ['kertas', 'botol', 'kaleng']

# Start video capture
cap = cv2.VideoCapture(1)
img_rows, img_cols = 60, 60
threshold = 0.6 # set your own threshold value here

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Resize frame to match the input shape of the model
    resized_frame = cv2.resize(frame, (img_rows, img_cols))

    # Preprocess the frame
    preprocessed_frame = resized_frame / 255.0

    # Add a batch dimension to the preprocessed frame
    preprocessed_frame = np.expand_dims(preprocessed_frame, axis=0)

    # Make predictions on the preprocessed frame
    predictions = model.predict(preprocessed_frame)

    # Get the class with the highest probability
    predicted_class = class_labels[np.argmax(predictions)]

    # Get the probability of the predicted class
    probability = np.max(predictions)

    # Check if the probability is above the threshold
    if probability > threshold:
        # Display the predicted class on the frame
        cv2.putText(frame, predicted_class, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 0), 2)
    else:
        # Display "No Object Detected" on the frame
        cv2.putText(frame, "No Object Detected", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 0, 255), 2)

    # Display the resulting frame
    cv2.imshow('frame', frame)

    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture and close all windows
cap.release()
cv2.destroyAllWindows()
