import cv2
import face_recognition as fr
import os
import numpy as np

# Create database
path = 'Day 14\\Empleados'
images = []
employee_names = []
employee_list = os.listdir(path)

for name in employee_list:
    current_image = cv2.imread(f'{path}\\{name}')
    images.append(current_image)
    employee_names.append(os.path.splitext(name)[0])

print(employee_names)

# Encode images
def encode(images):
    # Create new list
    encoded_list = []

    # Convert image to RGB
    for image in images:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        # Encode
        encoded = fr.face_encodings(image)[0]

        # Add to list
        encoded_list.append(encoded)

    # Return list
    return encoded_list

encoded_employee_list = encode(images)

# Capture image from camera
capture = cv2.VideoCapture(0, cv2.CAP_DSHOW)

# Read image from camera
success, image = capture.read()

if not success:
    print("Could not capture image")
else:
    # Recognize face in capture
    face_capture = fr.face_locations(image)

    face_capture_encoded = fr.face_encodings(image, face_capture)

    # Find matches
    for encoded_face, face_location in zip(face_capture_encoded, face_capture):
        matches = fr.compare_faces(encoded_employee_list, encoded_face)
        distance = fr.face_distance(encoded_employee_list, encoded_face)
        print(distance)
        match_index = np.argmin(distance)

        if distance[match_index] > 0.6:
            print("No match")
        else:
            name = employee_names[match_index]
            print(name)
            # Show captured image
            cv2.imshow("Image", image)

            # Keep window open
            cv2.waitKey(0)
            y1, x2, y2, x1 = face_location
            cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 3)
            cv2.putText(image, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
