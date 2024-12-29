#Slide Controller with Hand Gesture Recognition

This Python program allows you to control slides (Next/Previous) using hand gestures detected through your webcam. It uses Mediapipe for hand tracking and PyAutoGUI for simulating key presses to navigate slides seamlessly.

Features
	•	Hand Gesture Recognition:
	•	1 Finger Gesture (Index Finger Raised): Go to the next slide.
	•	2 Fingers Gesture (Index and Middle Finger Raised): Go to the previous slide.
	•	Works with popular presentation software like PowerPoint or Google Slides.
	•	Real-time feedback with hand landmarks drawn on the video feed.

 #Setup and Installation

Prerequisites
	•	Python 3.7 or higher
	•	A webcam connected to your computer
	•	Basic understanding of Python

 Installation
	1.	Clone the repository:
git clone https://github.com/gurpreetsinghwsu/slide_controller_hand_gesture.git
cd slide_controller_hand_gesture

.	Install dependencies:
pip install opencv-python mediapipe pyautogui

.	Run the program:
python slide_controller.py

How to Use
	1.	Start the Program:
	•	Connect your webcam and run the script.
	2.	Control Slides with Gestures:
	•	1 Finger Gesture (Index Finger Raised): Move to the next slide.
	•	2 Fingers Gesture (Index and Middle Fingers Raised): Go to the previous slide.
	3.	Stop the Program:
	•	Press the q key to exit the program.


 How It Works
	1.	Hand Tracking with Mediapipe:
	•	Detects landmarks on your hand in real-time using Mediapipe’s Hands module.
	2.	Gesture Recognition Logic:
	•	Identifies the number of fingers raised:
	•	1 Finger (Index Finger): Triggers a “Next Slide” action.
	•	2 Fingers (Index and Middle Fingers): Triggers a “Previous Slide” action.
	3.	Slide Control with PyAutoGUI:
	•	Simulates right and left arrow key presses to navigate slides.
