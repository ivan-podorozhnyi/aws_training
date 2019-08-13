import boto3
from modules import rds, s3

if __name__ == "__main__":
    s3_client = boto3.client('s3')
    sample_bucket = s3.create_bucket(s3_client, 'My_bucket')
    rds.create_rds(sample_bucket)
