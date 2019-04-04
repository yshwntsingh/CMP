import boto3
#from botocore.exceptions import ClientError
#import credentials

#consumer_secret = credentials.login['consumer_secret']
#ec2 = boto3.resource('ec2', region_name = 'us-east-2')

access_key = "***********"

secret_key = "***********************"

region='us-east-2'

client = boto3.client('ec2', aws_access_key_id=access_key, aws_secret_access_key=secret_key,

                                  region_name='us-east-2')
								  
ec2_regions = [region['RegionName'] for region in client.describe_regions()['Regions']]

#def get_session(region, access_id, secret_key):  
 #   return boto3.session.Session(region_name=region,
   #                             aws_access_key_id=access_id,
   #                             aws_secret_access_key=secret_key)
								
								
	
   # 3session = get_session(os.getenv('REGION'),
    #                      os.getenv('ACCESS_KEY_ID'),
    #                      os.getenv('SECRET_KEY'))
   # client = session.client('ec2')
    #resource = session.resource('ec2')
	
conn = boto3.resource('ec2', aws_access_key_id=access_key, aws_secret_access_key=secret_key,

                   region_name=region)
tag_purpose_test = {"Key": "Purpose", "Value": "Test"}
				   
#ec2 = boto3.resource('ec2')
instance = conn.create_instances(
    ImageId = 'ami-0c55b159cbfafe1f0',
    MinCount = 1,
    MaxCount = 1,
    InstanceType = 't2.micro',
    KeyName = 'cmp',
    SubnetId = 'subnet-049e3a1e39c0111e4',
	TagSpecifications=[{'ResourceType': 'instance',
                        'Tags': [tag_purpose_test]}])
											
for instance in instances:
		instance.add_tag('yash', 'prod')
print (instance[0].id)