# All-tracking

Combines several MediaPipe trackers (hands, pose, face mesh, holistic, face detection) behind a single `detector` class, and runs them on a live webcam feed with OpenCV.

## What it does

- One `detector` class that can be created in `hands`, `pose`, `face_mesh`, `holistic` or `face_detection` mode
- Holistic mode (the default in `all_tracking_utils.py`) draws pose, face mesh and left/right hand landmarks together
- Face detection mode draws a bounding box around each face
- Returns landmark pixel coordinates (`[id, x, y]`) and shows FPS on screen

The repo also contains `NEA_beat_algorithm.ipynb`, a separate Colab notebook experimenting with finding beats in a WAV file (smoothing, FFT and turning points with NumPy/SciPy). It is not connected to the tracking code, and the audio file it reads is not included.

## Tech

Python, OpenCV, MediaPipe (legacy `mp.solutions` API), NumPy. Notebook: pydub, SciPy, Matplotlib.

## Running it

```bash
pip install opencv-python mediapipe numpy
python all_tracking_utils.py
```

This runs holistic tracking on the webcam. To try another mode, change the argument to `detector(...)` in `main()`.

Notes:
- The scripts open camera index `1` (`cv2.VideoCapture(1)`). If you only have one webcam, change it to `0`.
- `all_tracking_ex.py` is set to `face_mesh` mode, which reads a result field (`face_landmarks`) that only the holistic model provides, so it does not work as-is. `fast_all_tracking.py` is empty.
- Written in 2021 against an older MediaPipe release.

This was an early learning project for getting familiar with MediaPipe and OpenCV.
