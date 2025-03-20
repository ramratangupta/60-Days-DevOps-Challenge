import boto3
import subprocess
import requests
from dotenv import load_dotenv
import os
load_dotenv(dotenv_path="../.env")
ec2 = boto3.client("ec2")
TAG = "log_monitoring"
key_file = "SSH_DAY7.pem"
ses = boto3.client("ses","us-east-1")

SLACK_WEBHOOK_URL = os.getenv("SLACK_WEBHOOK_URL")
def checkLogs(server):
    try:
        cmd = "grep -i 'error' /var/log/*.log | tail -n 10"
        ssh_cmd = f"ssh -i {key_file} ubuntu@{server['ip']} -o StrictHostKeyChecking=no '{cmd}'"
        errors = subprocess.check_output(ssh_cmd, shell=True, text=True)
        if errors!="":
           return {"instance_id":server['instance_id'],"logs":errors}
    except Exception as e:
        print(e)
def sendEmailNotification(errors):
    try:
        response = ses.send_email(
            Source="ramratan.gupta@gmail.com",
            Destination={"ToAddresses": ["ramratan.gupta@gmail.com"]},
            Message={
                "Subject": {"Data": "🚨 EC2 Log Monitoring Alert"},
                "Body": {"Text": {"Data": errors}}
            }
        )
        print("✅ Email alert sent!")
    except Exception as e:
        print(f"❌ Failed to send email: {e}")
def sendSlackNotification(errors):
    try:
        payload = {"text":errors}
        x = requests.post(SLACK_WEBHOOK_URL, json=payload)
        print(x)
    except Exception as e:
        print(f"❌ Failed to send email: {e}")
def monitorEC2():
    ips = getEC2Ips()
    error_logs = ""
    if len(ips)>0:
        for server in ips:
            errors = checkLogs(server)
            if errors!=None:
                error_logs=error_logs+f"\n\n\n🔴 {errors['instance_id']}\n\n{errors['logs']}"
        if len(error_logs)>0:
            #sendEmailNotification(error_logs)
            sendSlackNotification(error_logs)
    else:
        print("No Server found")
    
def getEC2Ips():
    ips = []
    ec2s = ec2.describe_instances(Filters=[{"Name": f"tag:{TAG}", "Values": ["*"]}, {"Name": "instance-state-name", "Values": ["running"]}])
    for Reservations in ec2s["Reservations"] :
        for instance in Reservations['Instances']:
            ips.append({"ip":instance["PublicIpAddress"],"instance_id":instance["InstanceId"]})
    return ips
if __name__ == "__main__":
    monitorEC2()