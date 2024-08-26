import os
import boto3
from google.cloud import storage
from file_uploader.config import S3_FILE_TYPES, GCS_FILE_TYPES, S3_CONFIG, GCS_CONFIG, AWS_S3_BUCKET_NAME, GOOGLE_CLOUD_BUCKET_NAME

def upload_to_s3(file_path):
    s3 = boto3.client('s3', 
                      aws_access_key_id=S3_CONFIG['aws_access_key_id'],
                      aws_secret_access_key=S3_CONFIG['aws_secret_access_key'],
                      region_name=S3_CONFIG['region_name'])
    s3.upload_file(file_path, AWS_S3_BUCKET_NAME, os.path.basename(file_path))

def upload_to_gcs(file_path):
    client = storage.Client.from_service_account_json(GCS_CONFIG['credentials_file'])
    bucket = client.bucket(GOOGLE_CLOUD_BUCKET_NAME)
    blob = bucket.blob(os.path.basename(file_path))
    blob.upload_from_filename(file_path)

def process_files(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            file_extension = file.split('.')[-1].lower()
            
            if file_extension in S3_FILE_TYPES:
                upload_to_s3(file_path)
            elif file_extension in GCS_FILE_TYPES:
                upload_to_gcs(file_path)
