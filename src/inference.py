import argparse
import time
from src.utils import read_video_frames, save_metrics_csv

def run_inference(video_path, model_path, out_csv='metrics.csv'):
    print(f"Running inference on {video_path} with model {model_path}")
    rows = []
    frame_count = 0
    for frame in read_video_frames(video_path):
        frame_count += 1
        # Placeholder: replace with model inference
        rows.append({'frame': frame_count, 'vehicles': 0})
    save_metrics_csv(rows, out_csv)
    print(f"Wrote metrics to {out_csv}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--video-path', required=True)
    parser.add_argument('--model-path', required=True)
    parser.add_argument('--out-csv', default='metrics.csv')
    args = parser.parse_args()
    run_inference(args.video_path, args.model_path, args.out_csv)
