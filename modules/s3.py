from troposphere import GetAtt
from troposphere.s3 import Bucket, PublicRead, VersioningConfiguration, \
    NotificationConfiguration, LambdaConfigurations

from .lambda_functions.lambdas3 import lambda_handler

bucket = Bucket("S3Bucket",
                AccessControl=PublicRead,
                VersioningConfiguration=VersioningConfiguration(Status="Enabled"),
                NotificationConfiguration=NotificationConfiguration(
                    LambdaConfigurations=[LambdaConfigurations(
                        Event='s3:ObjectCreated:*',
                        Function=GetAtt(lambda_handler, 'Arn'))]))
