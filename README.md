# Face Recognition System

This project is a simple face recognition system built using the **Face Recognition** library and **OpenCV**. It performs two key operations:

1. **Face Encoding**: It extracts face encodings from a collection of known images and saves them for future use.
2. **Face Recognition**: It compares the face encodings from unknown images against the known encodings and identifies matches.

The system utilizes **CNN-based** face detection for accurate recognition and is designed to be extensible for various use cases such as security systems, attendance tracking, or user identification.

---

## Project Overview

This project consists of two main components:

### 1. **Face Encoding (Training Phase)**:
   - Known faces are processed by loading images from a specified directory, detecting faces, and extracting face encodings.
   - The extracted encodings and corresponding names are saved in a `.npz` file for later use in face recognition.

### 2. **Face Recognition (Recognition Phase)**:
   - The system loads images from a directory of unknown faces, detects faces, and compares their encodings to the known encodings stored in the `.npz` file.
   - If a match is found, the name of the person is displayed on the image, and a rectangle is drawn around their face.
   - If no match is found, it labels the face as "Unknown."

---

## How It Works

1. **Training Phase**:
   - You first encode the faces of known individuals and save their encodings to a `.npz` file.
   
2. **Recognition Phase**:
   - When an unknown image is provided, the system detects faces, encodes them, and compares these encodings to the ones saved in the `.npz` file.
   - If a match is found, the person's name is displayed on the image; otherwise, it is labeled as "Unknown".

---

## Future Improvements

- **Real-time Face Recognition**: Extend this to work in real-time using a webcam or a video stream.
- **Improved Accuracy**: Experiment with different face recognition models and tweak the tolerance to improve matching accuracy.
- **GUI**: Implement a graphical user interface (GUI) for easier usage, especially for non-technical users.
- **Multiple Face Matching**: Handle images with multiple faces more efficiently by displaying the names of all detected faces.

---

## Conclusion

This face recognition system is designed to be simple and extensible, allowing you to add more faces, process unknown faces, and deploy the system in various real-world applications. It utilizes the powerful **face_recognition** library for face detection and encoding, with **OpenCV** for visualizing results.

If you found this project useful, feel free to give it a star on GitHub!

---
