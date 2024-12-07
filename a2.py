import face_recognition
import cv2
import numpy as np
import os

unknown_faces_dir = 'unknown'
tolerance = 0.45
model = 'cnn'
frame=4
font=2

arr = np.load('a.npz')
known_faces = arr['faces']
known_names = arr['names']

print('Processing unknown faces...')
for filename in os.listdir(unknown_faces_dir):
    print(filename)
    image = face_recognition.load_image_file(f'{unknown_faces_dir}/{filename}')
    locations = face_recognition.face_locations(image, model=model)
    encodings = face_recognition.face_encodings(image, locations)
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR) 

    for face_encoding, face_location in zip(encodings, locations):
        results = face_recognition.compare_faces(known_faces, face_encoding, tolerance)
        match = None

        if True in results:
            match = known_names[results.index(True)]
            print(f'match found: {match}')

            top_left = (face_location[3], face_location[0])
            bottom_right = (face_location[1], face_location[2])
            color = [0, 200, 0]
            cv2.rectangle(image, top_left, bottom_right, color, frame)

            top_left = (face_location[3], face_location[2])
            bottom_right = (face_location[1], face_location[2] + 22)
            cv2.rectangle(image, top_left, bottom_right, color, cv2.FILLED)

            cv2.putText(image, match, (face_location[3] + 10, face_location[2] + 15), 
                        cv2.FONT_HERSHEY_DUPLEX, 0.5, (110, 110, 110), font)

    cv2.imshow(filename, image)
    cv2.waitKey(10000)  