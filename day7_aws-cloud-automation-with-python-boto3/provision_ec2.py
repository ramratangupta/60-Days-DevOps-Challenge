import boto3
import os
import time
ec2 = boto3.client("ec2")
ec2_resource = boto3.resource("ec2")
INSTANCE_TYPE = "t2.micro"
AMI_ID = "ami-00bb6a80f01f03502"
SGNAME = "day7_sg_SSH"
EC2_KEYPAIR_NAME = "SSH_DAY7"
SSH_USERNAME = "ubuntu"
def createSecurtityGroup():

    #https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/create_security_group.html
    try:
        response = ec2.create_security_group(Description="SSH Connect example",GroupName=SGNAME)
        SecurityGroupID = response["GroupId"]
        response = ec2.authorize_security_group_ingress(
            GroupId=SecurityGroupID,
            IpPermissions=[
                {
                    'IpProtocol': 'tcp',
                    'FromPort': 22,
                    'ToPort': 22,                    
                    'IpRanges': [{"CidrIp": "0.0.0.0/0"}]
                },
            ],
        )
    except Exception as e:
        #https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/describe_security_groups.html
        response = ec2.describe_security_groups(GroupNames=[SGNAME])
        SecurityGroupID = response["SecurityGroups"][0]["GroupId"]
    return SecurityGroupID
def create_key_pair():
    try:
        key_pair = ec2.create_key_pair(KeyName=EC2_KEYPAIR_NAME)
        file = open(f"{EC2_KEYPAIR_NAME}.pem","w")
        file.write(key_pair["KeyMaterial"])
        os.chmod(f"{EC2_KEYPAIR_NAME}.pem",0o400)
    except Exception as e:
        pass
    return f"{EC2_KEYPAIR_NAME}.pem"

def check_ec2_via_ssh(instance_ip, key_file):
    """Connects to EC2 via SSH and checks its status."""
    print("🔍 Connecting to EC2 instance via SSH...")

    try:        
        output = os.system(f"ssh -i {key_file} ubuntu@{instance_ip} -o StrictHostKeyChecking=no 'uptime'")
        print(output)
    except Exception as e:
        print(f"❌ SSH Connection Failed: {e}")

def launch_ec2_instance(SecurityGroupID,SSHKEY):
    #https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/run_instances.html
    instance = ec2_resource.create_instances(
        ImageId=AMI_ID,
        InstanceType=INSTANCE_TYPE,
        MinCount=1,
        MaxCount=1,
        KeyName=SSHKEY,
        SecurityGroupIds=[SecurityGroupID],
        TagSpecifications=[{
            "ResourceType": "instance",
            "Tags": [{"Key": "Name", "Value": "MyEC2Instance"},{"Key": "log_monitoring", "Value": "Web Server"}]
        }]
    )[0]
    print(f"✅ EC2 instance launched with ID: {instance.id}")
    instance.wait_until_running()
    instance.reload()
    time.sleep(60)
    return instance.public_ip_address
    pass
SecurityGroupID = createSecurtityGroup()
SSHKEY = create_key_pair()
IP = launch_ec2_instance(SecurityGroupID,EC2_KEYPAIR_NAME)
check_ec2_via_ssh(IP,SSHKEY)