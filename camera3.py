import cv2
import numpy as np
import time
import tkinter as tk
import PoseModule as pm

# Initialize video capture and pose detector
cap = cv2.VideoCapture(0)
detector = pm.poseDetector()

def exercise_logic(exercise_func, total_rep=5):
    count = 0
    dir = 0
    frame_count = 0
    start_time = time.time()

    while count < total_rep:
        success, img = cap.read()
        if not success:
            raise Exception("Failed to read from camera")
        
        img = cv2.resize(img, (1288, 720))

        if frame_count % 5 == 0:
            img = detector.findPose(img, False)
            lmlist = detector.findPosition(img, False)
        
        frame_count += 1
        
        if len(lmlist) != 0:
            count, dir = exercise_func(img, lmlist, count, dir)

            # Check for crossing arms condition
            if check_crossed_arms(lmlist):
                save_image_with_counter(img, count)
                break

            cv2.putText(img, str(int(count)), (50, 100), cv2.FONT_HERSHEY_PLAIN, 5, (255, 0, 0), 5)

            elapsed_time = time.time() - start_time
            cv2.putText(img, f'Time: {int(elapsed_time)}s', (50, 150), cv2.FONT_HERSHEY_PLAIN, 5, (255, 0, 0), 5)

        cv2.imshow("Image", img)
        if cv2.waitKey(1) == ord('e'):
            break

def check_crossed_arms(lmlist):
    # Assuming lmlist[11] and lmlist[12] are the shoulder positions
    # lmlist[15] and lmlist[16] are the wrist positions

    left_shoulder = np.array([lmlist[11][1], lmlist[11][2]])  # Left shoulder (x, y)
    right_shoulder = np.array([lmlist[12][1], lmlist[12][2]])  # Right shoulder (x, y)
    left_wrist = np.array([lmlist[15][1], lmlist[15][2]])      # Left wrist (x, y)
    right_wrist = np.array([lmlist[16][1], lmlist[16][2]])     # Right wrist (x, y)

    # Check if wrists are on opposite sides of shoulders
    left_wrist_crossed = left_wrist[0] < right_shoulder[0] and left_wrist[1] > left_shoulder[1]
    right_wrist_crossed = right_wrist[0] > left_shoulder[0] and right_wrist[1] > right_shoulder[1]

    return left_wrist_crossed and right_wrist_crossed


def save_image_with_counter(img, count):
    cv2.putText(img, f'Counter: {int(count)}', (50, 200), cv2.FONT_HERSHEY_PLAIN, 5, (255, 0, 0), 5)
    cv2.imwrite("crossed_arms.png", img)  # Save image before closing
    print("Exercise terminated. Image saved as 'crossed_arms.png'.")
    
    # Release the video capture and close OpenCV windows
    cap.release()
    cv2.destroyAllWindows()

def push_up_logic(img, lmlist, count, dir):
    angle = detector.finfAngle(img, 11, 13, 15)  # Right arm elbow angle
    per = np.interp(angle, (185, 284), (0, 100))

    if per == 100 and dir == 0:
        count += 0.5
        dir = 1
    if per == 0 and dir == 1:
        count += 0.5
        dir = 0

    progress_bar = np.interp(angle, (185, 284), (0, img.shape[1]))
    cv2.rectangle(img, (50, 50), (int(progress_bar), 100), (0, 255, 0), -1)

    return count, dir

def squats_logic(img, lmlist, count, dir):
    angle = detector.finfAngle(img, 23, 25, 27)  # Left leg hip-knee-ankle angle
    per = np.interp(angle, (160, 270), (0, 100))  # Adjusted angle range for squat motion

    if per == 100 and dir == 0:
        count += 0.5
        dir = 1
    if per == 0 and dir == 1:
        count += 0.5
        dir = 0

    progress_bar = np.interp(angle, (160, 270), (0, img.shape[1]))
    cv2.rectangle(img, (50, 50), (int(progress_bar), 100), (0, 255, 0), -1)

    return count, dir

def jumping_jacks_logic(img, lmlist, count, dir):
    arm_angle = detector.finfAngle(img, 11, 13, 15)  # Right arm angle
    leg_angle = detector.finfAngle(img, 23, 25, 27)  # Left leg angle
    arm_per = np.interp(arm_angle, (170, 210), (0, 100))  # Adjust range for jumping jack arms
    leg_per = np.interp(leg_angle, (160, 230), (0, 100))  # Adjust range for jumping jack legs

    if arm_per == 100 and leg_per == 100 and dir == 0:
        count += 0.5
        dir = 1
    if arm_per == 0 and leg_per == 0 and dir == 1:
        count += 0.5
        dir = 0

    progress_bar = np.interp(arm_angle, (170, 210), (0, img.shape[1]))
    cv2.rectangle(img, (50, 50), (int(progress_bar), 100), (0, 255, 0), -1)

    return count, dir

def sit_up_logic(img, lmlist, count, dir):
    back_angle = detector.finfAngle(img, 11, 23, 25)  # Torso to hip angle
    per = np.interp(back_angle, (210, 310), (0, 100))  # Adjust range for sit-up

    if per == 100 and dir == 0:
        count += 0.5
        dir = 1
    if per == 0 and dir == 1:
        count += 0.5
        dir = 0

    progress_bar = np.interp(back_angle, (210, 310), (0, img.shape[1]))
    cv2.rectangle(img, (50, 50), (int(progress_bar), 100), (0, 255, 0), -1)

    return count, dir

def lunges_logic(img, lmlist, count, dir):
    angle = detector.finfAngle(img, 23, 25, 27)  # Left leg hip-knee-ankle angle
    per = np.interp(angle, (190, 280), (0, 100))  # Adjust range for lunges

    if per == 100 and dir == 0:
        count += 0.5
        dir = 1
    if per == 0 and dir == 1:
        count += 0.5
        dir = 0

    progress_bar = np.interp(angle, (190, 280), (0, img.shape[1]))
    cv2.rectangle(img, (50, 50), (int(progress_bar), 100), (0, 255, 0), -1)

    return count, dir

# Tkinter GUI
def start_exercise():
    selected_exercise = exercise_var.get()
    exercise_logic(exercises[selected_exercise])

root = tk.Tk()
root.title("AI Fitness Tracker")

# Dropdown menu to select the exercise
exercise_var = tk.StringVar()
exercise_var.set("Push-ups")
exercises = {
    "Push-ups": push_up_logic,
    "Squats": squats_logic,
    "Jumping Jacks": jumping_jacks_logic,
    "Sit-ups": sit_up_logic,
    "Lunges": lunges_logic
}

exercise_menu = tk.OptionMenu(root, exercise_var, *exercises.keys())
exercise_menu.pack()

# Start button to begin the selected exercise
start_button = tk.Button(root, text="Start Exercise", command=start_exercise)
start_button.pack()

# Run the Tkinter window
root.mainloop()

# Release the video capture and close OpenCV windows
cap.release()
cv2.destroyAllWindows()
