# 🖐️ Hand Gesture Recognition with MediaPipe

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![OpenCV](https://img.shields.io/badge/opencv-%23white.svg?style=for-the-badge&logo=opencv&logoColor=white)
![MediaPipe](https://img.shields.io/badge/MediaPipe-00ADD8?style=for-the-badge&logo=google&logoColor=white)
![Colab](https://img.shields.io/badge/Colab-F9AB00?style=for-the-badge&logo=googlecolab&color=525252)

An interactive Computer Vision pipeline that transforms your webcam into a gesture-controlled interface using Google's MediaPipe and Python.

---

## 🔴 Live Preview

<p align="center">
  <img src="https://github.com/user-attachments/assets/07ba6308-acb8-42b8-8962-b6192e0e0ebe" width="30%" />
  <img src="https://github.com/user-attachments/assets/b92dd127-b3a9-475b-bbeb-f8a393ed5f60" width="30%" />
  <img src="https://github.com/user-attachments/assets/b07bd9f6-4661-4bcc-ac70-979ebd00f8ed" width="30%" />
</p>

---

## 🔑 Key Features

* **⚡ Real-time Detection:** High-speed hand landmark tracking (21 unique points).
* **🌐 Colab Native:** Custom JavaScript bridge to access local webcams within virtual environments.
* **🧠 Logic-Based Classification:** Robust rule-based engine to identify:
    * `🖐 Open Palm` | `✌️ Peace` | `✊ Fist` | `👍 Thumbs Up` | `☝️ Pointing`
* **🎨 Augmented Overlay:** Dynamic rendering of the hand skeleton and gesture labels.

---

## 🛠️ How It Works



### The Pipeline
1.  **Capture:** JavaScript initiates a webcam stream and captures a frame.
2.  **Processing:** OpenCV converts images to RGB; MediaPipe maps 21 3D landmarks.
3.  **Inference:** * *Fingers:* Compares `TIP` vs `PIP` y-coordinates to determine "Extended" vs "Curled".
    * *Thumb:* Analyzes horizontal orientation relative to the palm base.
4.  **Feedback:** The system annotates the image and renders it instantly.

---

## 🚀 Getting Started

### 1. Launch Environment
Open this project in **Google Colab** to ensure the webcam JavaScript bridge executes correctly.

### 2. Install Dependencies
```bash
pip install mediapipe opencv-python numpy
