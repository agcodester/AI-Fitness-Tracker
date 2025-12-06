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
            cv2.putText(img, str(int(count)), (50, 100), cv2.FONT_HERSHEY_PLAIN, 5, (255, 0, 0), 5)

            elapsed_time = time.time() - start_time
            cv2.putText(img, f'Time: {int(elapsed_time)}s', (50, 150), cv2.FONT_HERSHEY_PLAIN, 5, (255, 0, 0), 5)

        cv2.imshow("Image", img)
        if cv2.waitKey(1) == ord('e'):
            break

# Push-up logic for both arms
def push_up_logic(img, lmlist, count, dir):
    # Right arm elbow angle
    right_angle = detector.finfAngle(img, 11, 13, 15)
    # Left arm elbow angle
    left_angle = detector.finfAngle(img, 12, 14, 16)

    right_per = np.interp(right_angle, (185, 284), (0, 100))
    left_per = np.interp(left_angle, (185, 284), (0, 100))

    if right_per == 100 and left_per == 100 and dir == 0:
        count += 0.5
        dir = 1
    if right_per == 0 and left_per == 0 and dir == 1:
        count += 0.5
        dir = 0

    progress_bar = np.interp((right_angle + left_angle) / 2, (185, 284), (0, img.shape[1]))
    cv2.rectangle(img, (50, 50), (int(progress_bar), 100), (0, 255, 0), -1)

    return count, dir

# Squats logic for both legs
def squats_logic(img, lmlist, count, dir):
    # Left leg hip-knee-ankle angle
    left_leg_angle = detector.finfAngle(img, 23, 25, 27)
    # Right leg hip-knee-ankle angle
    right_leg_angle = detector.finfAngle(img, 24, 26, 28)

    left_per = np.interp(left_leg_angle, (160, 270), (0, 100))
    right_per = np.interp(right_leg_angle, (160, 270), (0, 100))

    if left_per == 100 and right_per == 100 and dir == 0:
        count += 0.5
        dir = 1
    if left_per == 0 and right_per == 0 and dir == 1:
        count += 0.5
        dir = 0

    progress_bar = np.interp((left_leg_angle + right_leg_angle) / 2, (160, 270), (0, img.shape[1]))
    cv2.rectangle(img, (50, 50), (int(progress_bar), 100), (0, 255, 0), -1)

    return count, dir

# Jumping Jacks logic for both arms and legs
def jumping_jacks_logic(img, lmlist, count, dir):
    # Right arm angle
    right_arm_angle = detector.finfAngle(img, 11, 13, 15)
    # Left arm angle
    left_arm_angle = detector.finfAngle(img, 12, 14, 16)
    # Right leg angle
    right_leg_angle = detector.finfAngle(img, 24, 26, 28)
    # Left leg angle
    left_leg_angle = detector.finfAngle(img, 23, 25, 27)

    arm_per = np.interp((right_arm_angle + left_arm_angle) / 2, (170, 210), (0, 100))
    leg_per = np.interp((right_leg_angle + left_leg_angle) / 2, (160, 230), (0, 100))

    if arm_per == 100 and leg_per == 100 and dir == 0:
        count += 0.5
        dir = 1
    if arm_per == 0 and leg_per == 0 and dir == 1:
        count += 0.5
        dir = 0

    progress_bar = np.interp((right_arm_angle + left_arm_angle) / 2, (170, 210), (0, img.shape[1]))
    cv2.rectangle(img, (50, 50), (int(progress_bar), 100), (0, 255, 0), -1)

    return count, dir

# Sit-ups logic for torso and both legs
def sit_up_logic(img, lmlist, count, dir):
    # Torso to hip angle
    back_angle = detector.finfAngle(img, 11, 23, 25)
    # Hip to knee angle for both legs
    left_leg_angle = detector.finfAngle(img, 23, 25, 27)
    right_leg_angle = detector.finfAngle(img, 24, 26, 28)

    per = np.interp(back_angle, (210, 310), (0, 100))

    if per == 100 and dir == 0:
        count += 0.5
        dir = 1
    if per == 0 and dir == 1:
        count += 0.5
        dir = 0

    progress_bar = np.interp((left_leg_angle + right_leg_angle) / 2, (210, 310), (0, img.shape[1]))
    cv2.rectangle(img, (50, 50), (int(progress_bar), 100), (0, 255, 0), -1)

    return count, dir

# Lunges logic for both legs
def lunges_logic(img, lmlist, count, dir):
    # Left leg hip-knee-ankle angle
    left_leg_angle = detector.finfAngle(img, 23, 25, 27)
    # Right leg hip-knee-ankle angle
    right_leg_angle = detector.finfAngle(img, 24, 26, 28)

    left_per = np.interp(left_leg_angle, (190, 280), (0, 100))
    right_per = np.interp(right_leg_angle, (190, 280), (0, 100))

    if left_per == 100 and right_per == 100 and dir == 0:
        count += 0.5
        dir = 1
    if left_per == 0 and right_per == 0 and dir == 1:
        count += 0.5
        dir = 0

    progress_bar = np.interp((left_leg_angle + right_leg_angle) / 2, (190, 280), (0, img.shape[1]))
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
