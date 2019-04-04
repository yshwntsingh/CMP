import boto3
import os
#from botocore.exceptions import ClientError
#import credentials

#consumer_secret = credentials.login['consumer_secret']
#ec2 = boto3.resource('ec2', region_name = 'us-east-2')

access_key = "*********"

secret_key = "*******************"

os.environ['AWS_DEFAULT_REGION'] = 'eu-east-2'

#region='us-east-1'
#client = boto3.client('s3')

#client = boto3.client('s3', aws_access_key_id=access_key, aws_secret_access_key=secret_key,

 #                                 region_name='us-east-2')
								  
s3 = boto3.client('s3', aws_access_key_id=access_key, aws_secret_access_key=secret_key,
                                    region_name='os.environ['AWS_DEFAULT_REGION']')

                                   
								  
#ec2_regions = [region['RegionName'] for region in client.describe_regions()['Regions']]

#def get_session(region, access_id, secret_key):  
 #   return boto3.session.Session(region_name=region,
   #                             aws_access_key_id=access_id,
   #                             aws_secret_access_key=secret_key)
								
								
	
   # 3session = get_session(os.getenv('REGION'),
    #                      os.getenv('ACCESS_KEY_ID'),
    #                      os.getenv('SECRET_KEY'))
   # client = session.client('ec2')
    #resource = session.resource('ec2')
	
#conn = boto3.resource('s3', aws_access_key_id=access_key, aws_secret_access_key=secret_key)
#tag_purpose_test = {"Key": "Purpose", "Value": "Test"}
				   
#ec2 = boto3.resource('ec2')

#import boto3

#client = boto3.client('s3')

#response = client.create_bucket(
    #ACL='private'|'public-read'|'public-read-write'|'authenticated-read',
    #Bucket='string',
    #CreateBucketConfiguration={
     #  'LocationConstraint': 'EU'|'eu-west-1'|'us-west-1'|'us-west-2'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'sa-east-1'|'cn-north-1'|'eu-central-1'
#},
#GrantFullControl='string',
#GrantRead='string',
#GrantReadACP='string',
#GrantWrite='string',
#GrantWriteACP='string'
#)
#s3 = boto3.client('s3')
s3 = s3.create_bucket('cmp', CreateBucketConfiguration={'LocationConstraint': AWS_DEFAULT_REGION})




print (s3[0].id)