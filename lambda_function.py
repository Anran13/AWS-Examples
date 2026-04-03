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
# 1. 安裝套件（會產生 __pycache__）
# pip install -t . boto3 requests urllib3
# 2. 刪除 __pycache__
# 刪除所有 .pyd、.so、__pycache__、.egg-info
# Remove-Item -Recurse -Force __pycache__ -ErrorAction SilentlyContinue
# Remove-Item -Recurse -Force *.pyd -ErrorAction SilentlyContinue
# Remove-Item -Recurse -Force *.egg-info -ErrorAction SilentlyContinue
# Remove-Item -Recurse -Force *.dist-info -ErrorAction SilentlyContinue
# 再打包
# Compress-Archive -Path * -DestinationPath awslambdademo.zip
# powershell Compress-Archive -Path * -DestinationPath awslambdademo.zip