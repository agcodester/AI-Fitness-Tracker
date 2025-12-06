AI Fitness Tracker
===================

A real-time AI-powered exercise tracking system built using OpenCV, Tkinter,
and a custom PoseModule for pose estimation. The app detects joint angles from
webcam input and automatically counts repetitions for various exercises.

----------------------------------------
FEATURES
----------------------------------------
- Real-time pose detection using webcam
- Automatic rep counting via angle-based motion logic
- Supports 5 exercises: Push-ups, Squats, Jumping Jacks, Sit-ups, Lunges
- Tkinter GUI for selecting exercises
- OpenCV feedback window with:
  - Rep counter
  - Progress bar
  - Timer

----------------------------------------
PROJECT STRUCTURE
----------------------------------------
CV-PROJECT/
├── PoseModule.py
├── camera.py
├── camera2.py
├── camera3.py
├── camera4.py
└── __pycache__/

----------------------------------------
TECHNOLOGIES USED
----------------------------------------
- Python 3
- OpenCV
- NumPy
- Tkinter
- Custom Pose Detection Module (PoseModule)

----------------------------------------
HOW TO RUN
----------------------------------------
1. Install dependencies:
   ```bash
   pip install opencv-python numpy
  
3. Run the main script:
   ```bash
   python camera2.py

5. Use the Tkinter UI:
   - Select exercise
   - Click Start Exercise
   - Press 'e' in the webcam window to exit

----------------------------------------
HOW IT WORKS
----------------------------------------
- Detects body landmarks
- Calculates joint angles
- Maps angles to motion percentage
- Tracks direction (up/down)
- Counts each full repetition

----------------------------------------
SUPPORTED EXERCISES
----------------------------------------
- Push-ups
- Squats
- Jumping Jacks
- Sit-ups
- Lunges
