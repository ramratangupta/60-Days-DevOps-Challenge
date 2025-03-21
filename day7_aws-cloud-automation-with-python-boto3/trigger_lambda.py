import boto3
import json

# AWS Configuration
AWS_REGION = "us-east-1" 
LAMBDA_FUNCTION_NAME = "send_email" 

# Initialize the AWS Lambda client
lambda_client = boto3.client("lambda", region_name=AWS_REGION)

def invoke_lambda(payload={}):
    """Invokes the AWS Lambda function with an optional JSON payload."""
    print(f"🚀 Triggering Lambda function: {LAMBDA_FUNCTION_NAME}")
    
    try:
        response = lambda_client.invoke(
            FunctionName=LAMBDA_FUNCTION_NAME,
            InvocationType="RequestResponse",  # Use "Event" for async invocation
            Payload=json.dumps(payload)
        )
        
        # Read response
        response_payload = json.loads(response["Payload"].read().decode())
        print(f"✅ Lambda response: {response_payload}")
    
    except Exception as e:
        print(f"❌ Failed to invoke Lambda: {e}")

if __name__ == "__main__":
    # Example payload
    payload = {"message": "Hello from Python!"}
    
    invoke_lambda(payload)