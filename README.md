# AI Object Tracking using YOLO

An AI-based object tracking project that uses the **YOLO object detection model** and **OpenCV** to detect and track multiple objects in a video. The system assigns unique tracking IDs to detected objects and maintains their identities across consecutive frames.

## Project Overview

This project was developed as **Task 4 of the CodeAlpha AI Internship**.

The system processes a video frame by frame, detects objects using YOLO, tracks detected objects across frames, displays tracking information, and saves the processed video as an output file.

The project demonstrates the practical application of **Artificial Intelligence and Computer Vision** for object detection and tracking.

## Features

* AI-based object detection using YOLO
* Real-time object tracking across video frames
* Unique tracking IDs for detected objects
* Detection of multiple objects in a single frame
* Video processing using OpenCV
* Live display of tracking results
* Saves the final tracked video
* Supports tracking of objects such as people and vehicles

## Technologies Used

* Python
* Ultralytics YOLO
* OpenCV
* Computer Vision
* Artificial Intelligence

## Project Workflow

```text
Input Video
     ↓
Read Video Frames using OpenCV
     ↓
YOLO Object Detection
     ↓
Object Tracking
     ↓
Assign Tracking IDs
     ↓
Annotate Detected Objects
     ↓
Display Tracking Results
     ↓
Save Tracked Video
```

## Project Structure

```text
AI_Object_Tracking/
│
├── input/
│   └── test_video.mp4
│
├── output/
│   └── tracked_video.avi
│
├── detector.py
├── yolo26n.pt
└── README.md
```

## Model

The project uses a **YOLO-based object detection model** through the Ultralytics framework.

The model is loaded using:

```python
from ultralytics import YOLO

model = YOLO("yolo26n.pt")
```

For tracking, the model uses:

```python
results = model.track(frame, persist=True)
```

The `persist=True` parameter allows object identities to be maintained across consecutive video frames.

## Input

The input video is stored in:

```text
input/test_video.mp4
```

The system reads the video frame by frame and processes each frame using the YOLO model.

## Output

The processed tracking video is saved in:

```text
output/tracked_video.avi
```

The output video contains:

* Detected objects
* Bounding boxes
* Object labels
* Tracking IDs

## Installation

Create a virtual environment:

```bash
python -m venv venv
```

### Activate the Virtual Environment

For Windows:

```bash
venv\Scripts\activate
```

## Install Dependencies

Install the required Python libraries:

```bash
pip install ultralytics opencv-python
```

## How to Run

Run the object tracking program with:

```bash
python detector.py
```

The program will:

1. Load the YOLO model
2. Open the input video
3. Detect objects in each frame
4. Track objects across frames
5. Display the annotated video
6. Save the tracking output

The final output will be saved as:

```text
output/tracked_video.avi
```

## Example Tracking Result

The system can detect and track multiple objects, for example:

```text
Person 0
Person 1
Car 2
```

The numbers represent the tracking IDs assigned to individual objects.

## Applications

Object tracking can be used in various real-world applications, including:

* Traffic monitoring
* People counting
* Surveillance systems
* Vehicle tracking
* Smart city applications
* Retail analytics
* Sports analysis
* Computer vision research

## Internship

**CodeAlpha AI Internship — Task 4: Object Tracking**

This project demonstrates the practical use of AI and computer vision techniques for detecting and tracking objects in video using YOLO and OpenCV.

## Author

**Zoya Ali**

GitHub: `Zoya456259`
