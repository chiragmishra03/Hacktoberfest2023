#Creating a QR code scanner in Python using external libraries to capture images from your device's camera, 
#process the image to detect QR codes, and then extract the information from them. In this example, 
#I'll use the OpenCV library for image capture and processing, and the pyzbar library to decode QR codes. 
#You can install these libraries using pip:

pip install opencv-python-headless pyzbar


#Python script to create a QR code scanner:

import cv2
from pyzbar.pyzbar import decode

# Initialize the camera
cap = cv2.VideoCapture(0)

while True:
    # Capture a frame
    ret, frame = cap.read()

    if not ret:
        continue

    # Decode QR codes in the frame
    decoded_objects = decode(frame)

    for obj in decoded_objects:
        qr_data = obj.data.decode('utf-8')
        print(f"QR Code Data: {qr_data}")

    # Display the frame
    cv2.imshow("QR Code Scanner", frame)

    # Exit the loop if the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close the OpenCV window
cap.release()
cv2.destroyAllWindows()

