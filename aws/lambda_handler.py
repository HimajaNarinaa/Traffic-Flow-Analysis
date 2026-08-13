import os
import json
from aws.s3_helper import download_s3_file, upload_s3_file
from src.inference import run_inference

def handler(event, context):
    # Expected event keys: bucket, key, model_key
    bucket = event.get('bucket')
    key = event.get('key')
    model_key = event.get('model_key', 'models/model.pth')
    tmp_video = '/tmp/input.mp4'
    tmp_model = '/tmp/model.pth'
    if not download_s3_file(bucket, key, tmp_video):
        return {'statusCode': 500, 'body': 'failed to download video'}
    if not download_s3_file(bucket, model_key, tmp_model):
        # continue with default model if model download fails
        tmp_model = model_key
    out_csv = '/tmp/metrics.csv'
    run_inference(tmp_video, tmp_model, out_csv=out_csv)
    upload_s3_file(bucket, f"outputs/{os.path.basename(key)}.csv", out_csv)
    return {'statusCode': 200, 'body': json.dumps({'metrics': f"outputs/{os.path.basename(key)}.csv"})}
