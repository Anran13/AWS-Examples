import os 
import boto3
import requests

def lambda_handler(event, context):
    bucket_name = os.environ.get('BUCKET_NAME')
    content = requests.get('https://data.gharchive.org/2015-01-01-15.json.gz').content
    s3_client = boto3.client('s3')
    s3_client.put_object(
        Body=content,
        bucket=bucket_name,
        Key='lambdademo/2015-01-01-15.json.gz',
    )

# execute in command line to create zip file for lambda deployment (change to powershell terminal)
# python -m venv old-env (create virtual environment)
# drug old-env\Scripts\activate.bat into our cmd terminal
# pip install requests -t . (install dependencies to current directory)
# pip install boto3
# check if the python have requests and boto3
# python (enter python shell)
# import requests
# import boto3)
# change to git-bash terminal
# zip -r awslambdademo.zip . -x old-env/\*
