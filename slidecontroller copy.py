import cv2
import mediapipe as mp
import pyautogui

# Initialize Mediapipe Hands
mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils
hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)


# Define a function to detect gestures
def detect_gesture(landmarks):
    # Get the tip positions of thumb and index fingers
    thumb_tip = landmarks[4]
    index_tip = landmarks[8]

    # Calculate the distance between thumb and index tip
    distance = ((thumb_tip.x - index_tip.x) ** 2 + (thumb_tip.y - index_tip.y) ** 2) ** 0.5

    # Threshold for pinching gesture
    if distance < 0.05:
        return "pinch"  # Recognized as a pinching gesture
    elif index_tip.y < landmarks[6].y:  # If index tip is above the hand
        return "swipe up"
    elif index_tip.y > landmarks[6].y and thumb_tip.y > landmarks[6].y:
        return "swipe down"
    else:
        return None


# Start capturing from the webcam
cap = cv2.VideoCapture(1)

print("Use gestures to control slides:")
print("1. Swipe up - Go to next slide")
print("2. Swipe down - Go to previous slide")

while True:
    success, frame = cap.read()
    if not success:
        break

    # Flip the frame for a mirrored effect
    frame = cv2.flip(frame, 1)
    h, w, c = frame.shape

    # Convert the frame to RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process the frame for hand landmarks
    results = hands.process(rgb_frame)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            # Draw hand landmarks on the frame
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Get normalized landmark positions
            landmarks = hand_landmarks.landmark

            # Detect gesture
            gesture = detect_gesture(landmarks)

            if gesture == "swipe up":
                pyautogui.press("right")  # Go to the next slide
                print("Next Slide")
            elif gesture == "swipe down":
                pyautogui.press("left")  # Go to the previous slide
                print("Previous Slide")

    # Show the frame
    cv2.imshow("Hand Gesture Control", frame)

    # Break the loop on pressing 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()