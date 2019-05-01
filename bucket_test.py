import boto3

AWS_ACCESS = "AKIA3OK3Q246VRPJEFHO"

AWS_SECRET = "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"

s3_client = boto3.client('s3',
        aws_access_key_id=AWS_ACCESS,
        aws_secret_access_key=AWS_SECRET)

def upload_to_bucket(filename, directory = ''): #Reliant on relative pathing or specified directory
    response = s3_client.upload_file(directory+filename, 'ece498icc', filename)


upload_to_bucket('faceDetection.py')

