import boto3
import subprocess


def zip_lambda(archive_name, lambda_file):
    subprocess.call(["zip", archive_name, lambda_file])

lambda_client = boto3.client('lambda')

fn_name = "HelloWorld"
fn_role = 'arn:aws:iam::950440424238:role/LambdaBasicExecution'



lambda_client.create_function(
    FunctionName=fn_name,
    Runtime='python2.7',
    Role=fn_role,
    Handler="{0}.lambda_handler".format(fn_name),
    Code={'ZipFile': open("{0}.zip".format(fn_name), 'rb').read(), },
)