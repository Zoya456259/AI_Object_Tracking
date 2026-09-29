import cv2
from ultralytics import YOLO
import os

model = YOLO("yolo26n.pt")

video = cv2.VideoCapture("input/test_video.mp4")

fps = video.get(cv2.CAP_PROP_FPS)
width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))

os.makedirs("output", exist_ok=True)

fourcc = cv2.VideoWriter_fourcc(*"XVID")

out = cv2.VideoWriter(
    "output/tracked_video.avi",
    fourcc,
    fps,
    (width, height)
)

while True:
    success, frame = video.read()

    if not success:
        break

    results = model.track(frame, persist=True)

    annotated_frame = results[0].plot()

    out.write(annotated_frame)

    cv2.imshow("Object Tracking", annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

video.release()
out.release()
cv2.destroyAllWindows()