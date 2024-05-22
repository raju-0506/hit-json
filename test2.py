import boto3

# Initialize the EC2 client
ec2 = boto3.client('ec2', region_name='us-east-1')  # Replace 'your_region' with your desired AWS region

# Specify parameters for the instance
instance_params = {
    'ImageId': 'ami-04b70fa74e45c3917',  # Specify the AMI ID of the instance you want to launch
    'InstanceType': 't2.micro',  # Specify the instance type
    'KeyName': 'ubuntu/images/hvm-ssd-gp3/ubuntu-noble-24.04-amd64-server-20240423',  
    # Replace 'your_key_pair_name' with your EC2 key pair name
    'MinCount': 1,
    'MaxCount': 1
}

# Create the EC2 instance
response = ec2.run_instances(**instance_params)

# Extract the instance ID from the response
instance_id = response['Instances'][0]['InstanceId']

print("Instance created with ID:", instance_id)
