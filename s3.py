import logging
from botocore.exceptions import ClientError


def create_bucket(client, bucket_name, enable_versioning=True):
    """Create an S3 bucket

    :param enable_versioning: option to enable versioning
    :param client: S3 client
    :param bucket_name: Bucket to create
    :return: Instance of bucket if bucket created, else False
    """

    try:
        bucket = client.create_bucket(Bucket=bucket_name)
        if enable_versioning:
            client.BucketVersioning(bucket_name).enable()

    except ClientError as e:
        logging.error(e)
        return False
    return bucket
