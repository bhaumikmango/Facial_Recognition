import face_recognition
import os
import numpy as np

known_faces_dir = 'drive-download-20241125T085515Z-001'

print('Loading known faces...')
known_faces = []
known_names = []

for name in os.listdir(known_faces_dir):
    for filename in os.listdir(f'{known_faces_dir}/{name}'):
        try:
            image = face_recognition.load_image_file(f'{known_faces_dir}/{name}/{filename}')

            encodings = face_recognition.face_encodings(image)

            if encodings:
                known_faces.append(encodings[0])
                known_names.append(name)
                print(f'Face detected in {known_faces_dir}/{name}/{filename}')
            else:
                print(f'No face detected in {known_faces_dir}/{name}/{filename}')

        except Exception as e:
            print(f'Error processing {known_faces_dir}/{name}/{filename}: {e}')

known_faces = np.array(known_faces)
known_names = np.array(known_names)

np.savez('a.npz', faces=known_faces, names=known_names)

print('Known faces and names saved successfully.')