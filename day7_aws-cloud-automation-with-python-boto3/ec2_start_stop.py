import boto3
region = input("Please input region to run : ")
#region = "ap-south-1"
ec2 = boto3.client("ec2",region)
instances = ec2.describe_instances(Filters=[{"Name":"instance-state-name","Values":['pending','running','stopped']}])

for Reservations in instances["Reservations"]:
    for instance in Reservations["Instances"]:
        print(f"Current State {instance['State']}")
        if instance["State"]["Name"] == "stopped":
            st = ec2.start_instances(InstanceIds=[instance["InstanceId"]])["StartingInstances"][0]["CurrentState"]
        else:
            st = ec2.stop_instances(InstanceIds=[instance["InstanceId"]])["StoppingInstances"][0]["CurrentState"]
        print(st)