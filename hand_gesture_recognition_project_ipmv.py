# Hand Gesture Recognition using MediaPipe

This project uses Google Colab to capture an image from a webcam, detect a hand using the MediaPipe library, and recognize a specific gesture. The recognized gesture and the hand landmarks are then displayed on the output image.

![Hand Gesture Recognition Demo](https://i.imgur.com/gYdI6nS.png)
*Note: You can replace the image URL with a screenshot of your own project running.*

---
## 📜 Description

The script is designed to run in a Google Colab environment. It leverages JavaScript to access the user's webcam for image capture. Once an image is captured, it utilizes the powerful **MediaPipe Hands** solution to detect the presence and landmarks of a hand.

A custom logic function then analyzes the spatial relationship of these landmarks to classify the hand's pose into one of several predefined gestures. This project serves as an excellent introduction to computer vision and gesture recognition.

---
## ✨ Features

- **Webcam Integration in Colab:** Captures a single image directly from your webcam within a Google Colab notebook.
- **Hand Landmark Detection:** Uses MediaPipe to accurately identify 21 key 3D landmarks of the hand.
- **Gesture Classification:** Implements a rule-based algorithm to recognize the following gestures:
    - 🖐 Open Palm
    - ✌️ Peace Sign
    - ✊ Fist
    - 👍 Thumbs Up
    - ☝️ Pointing
- **Visual Feedback:** Overlays the detected landmarks and the name of the recognized gesture onto the captured image for clear visualization.

---
## ⚙️ How It Works

The process can be broken down into four main steps:

1.  **Setup & Dependencies:** The first few cells install the necessary Python libraries, including `mediapipe`, `opencv-python`, and `numpy`.

2.  **Image Capture:** A JavaScript function is executed within the Colab environment to request webcam access from the user. It captures a single frame and passes it back to the Python environment as a base64 encoded image, which is then decoded into an OpenCV-compatible format.

3.  **Hand Detection:**
    - The captured image is converted from BGR to RGB color space, as MediaPipe expects RGB input.
    - The `mp.solutions.hands.Hands` model processes the image to find hand landmarks.
    - If a hand is detected, the model returns the coordinates for all 21 landmarks.

4.  **Gesture Recognition:**
    - The custom `recognize_gesture()` function is called with the detected landmarks.
    - It determines the state of each finger (extended or curled) by comparing the vertical position (y-coordinate) of the fingertip to the joint below it.
    - It checks the thumb's state by comparing the horizontal position (x-coordinate) of the thumb tip relative to a lower joint.
    - Based on the combination of these finger and thumb states, it returns the corresponding gesture as a string.

5.  **Display Output:** The final image, annotated with the hand skeleton and the recognized gesture text, is displayed in the Colab output cell.

---
## 🚀 How to Run

1.  **Open in Google Colab:** Ensure the `.ipynb` file is open in a Google Colab environment.
2.  **Install Dependencies:** Run the first few cells containing `!pip install ...` commands to set up the required libraries.
3.  **Run the Main Script:** Execute the main code cell (starting from `STEP 2: Import required libraries`).
4.  **Grant Camera Permission:** Your browser will ask for permission to use your camera. Click **"Allow"**.
5.  **Capture Image:** A video stream from your webcam will appear. The script will automatically capture one frame.
6.  **View Result:** The script will process the frame and display the output image below the code cell, showing your hand with the detected gesture labeled.

---
## 📋 Requirements

The project requires the following Python libraries:

- `mediapipe==0.10.11`
- `opencv-python`
- `numpy`

These are all installed by the commands at the beginning of the provided notebook.
