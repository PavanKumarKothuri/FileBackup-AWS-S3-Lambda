import boto3
import os
import logging

# Set up logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Initialize the S3 client
s3_client = boto3.client('s3')

def lambda_handler(event, context):
    """
    Function to back up files from source S3 bucket to destination S3 bucket
    whenever a new file is uploaded.
    """
    # Log the event details
    logger.info(f"Event received: {event}")
    
    # Extract bucket name and object key from the event
    source_bucket = event['Records'][0]['s3']['bucket']['name']
    object_key = event['Records'][0]['s3']['object']['key']
    
    # Define the destination bucket
    destination_bucket = "destination-bucket-yourname"  # Replace with your destination bucket name
    
    try:
        # Copy the object to the destination bucket
        copy_source = {'Bucket': source_bucket, 'Key': object_key}
        s3_client.copy_object(CopySource=copy_source, Bucket=destination_bucket, Key=object_key)
        
        logger.info(f"File {object_key} backed up from {source_bucket} to {destination_bucket}")
        return {"status": "success", "message": f"File {object_key} backed up successfully."}
    
    except Exception as e:
        logger.error(f"Error during backup: {e}")
        return {"status": "error", "message": str(e)}