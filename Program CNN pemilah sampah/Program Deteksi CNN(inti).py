import cv2
import tensorflow as tf
import numpy as np
import serial

port = 'COM7'  # Ubah sesuai dengan port serial yang digunakan
baud_rate = 9600  # Sesuaikan dengan baud rate pada perangkat

# Inisialisasi objek serial
ser = serial.Serial(port, baud_rate)

# Load model
model = tf.keras.models.load_model('D:\Project-project\Pemilah Sampah\Datasheet created\datasheet1405_next.h5')

# Define class labels
class_labels = ['botol','kaleng', 'kertas']
labels = "prepare"

# Start video capture
cap = cv2.VideoCapture(1)
img_rows, img_cols = 120, 120

threshold_kertas = 75 # set your own threshold value here
threshold_kaleng = 80
threshold_botol = 80

kondisi = 0

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

    # Get the probabilities for each class
    class_probabilities = predictions[0]

    # Display the predicted class and its probability for each class
    for i, class_probability in enumerate(class_probabilities):
        class_label = class_labels[i]
        probability = class_probability * 100
        print(f"{class_label}: {probability:.2f}%")

        if class_label == 'kertas' and probability > threshold_kertas:
            cv2.putText(frame, "Kertas", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255 ,0), 2)
            # Kirim data ke perangkat
            ser.write(b'1\n')
            kondisi = 1
        elif class_label == 'kaleng' and probability > threshold_kaleng:
            cv2.putText(frame, "kaleng", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255 ,0), 2)
            # Kirim data ke perangkat
            ser.write(b'3\n')
            kondisi = 1
        elif class_label == 'botol' and probability > threshold_botol:
            cv2.putText(frame, "botol", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 0), 2)
            # Kirim data ke perangkat
            ser.write(b'2\n')
            kondisi = 1

    if kondisi == 0:
        cv2.putText(frame, "No Objet Detection", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 0, 255), 2)
        # Kirim data ke perangkat
        ser.write(b' \n')
    kondisi = 0


    # Display the resulting frame
    cv2.imshow('frame', frame)

    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'): 
        break

# Release the capture and close all windows
cap.release()
cv2.destroyAllWindows()