import boto3
route53 = boto3.client("route53")
from dotenv import load_dotenv
import os
load_dotenv(dotenv_path="../.env")
HOSTED_ZONE_ID = os.getenv("HOSTED_ZONE_ID")
IP = "127.0.0.1"
domain="rds.local"
RECORD_TYPE = "A"
TTL = 0
change_batch = {
        "Changes": [
            {
                "Action": "UPSERT",
                "ResourceRecordSet": {
                    "Name": domain,
                    "Type": RECORD_TYPE,
                    "TTL": TTL,
                    "ResourceRecords": [{"Value": IP}]
                }
            }
        ]
    }

try:
    response = route53.change_resource_record_sets(
        HostedZoneId=HOSTED_ZONE_ID,
        ChangeBatch=change_batch
    )
    print(f"✅ DNS record updated! Change ID: {response['ChangeInfo']['Id']}")
except Exception as e:
    print(f"❌ Failed to update DNS record: {e}")