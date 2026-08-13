import cv2
import numpy as np
import time

def read_video_frames(path):
    cap = cv2.VideoCapture(path)
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        yield frame
    cap.release()

def save_metrics_csv(rows, path):
    import csv
    keys = rows[0].keys() if rows else []
    with open(path, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=list(keys))
        writer.writeheader()
        writer.writerows(rows)
