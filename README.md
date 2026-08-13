# Traffic Flow Analysis

Trained an object detection model and a scaffolded pipeline for camera-based congestion analysis.

Overview

- Trained an object detection model & implemented a DeepStream-based pipeline on a self-annotated vehicle dataset.
- Trained using CNN + attention mechanisms achieving ~85% precision and ~35% recall across classes (replace with your exact metrics).
- Processes camera video streams, computes congestion metrics, and logs runs to PostgreSQL. Supports S3-based artifacts and an AWS Lambda inference entrypoint.

Repository structure

- `src/` — training and inference scripts (placeholders)
- `aws/` — Lambda handler and S3 helpers
- `db/`  — PostgreSQL schema for logs
- `models/` — trained models (not included)
- `Dockerfile`, `requirements.txt`, `.gitignore`

Quick start

1. Create a virtualenv and install dependencies:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

2. Train a (placeholder) model:

```bash
python src/train.py --epochs 1 --save-path models/model.pth
```

3. Run inference on a local video:

```bash
python src/inference.py --video-path assets/sample.mp4 --model-path models/model.pth
```

4. To deploy the Lambda function, package `aws/` and set an IAM role allowing S3 and (optionally) RDS access.

Notes

- This scaffold contains working placeholders and utilities. Replace the placeholder model, dataset, and DeepStream configs with your production artifacts.

License: MIT

