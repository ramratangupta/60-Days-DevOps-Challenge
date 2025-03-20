import boto3
from datetime import datetime
s3 = boto3.client("s3","us-east-1")
def createBucket(name):
    isBucketCreated = False
    try:
        out = s3.create_bucket(Bucket=name)
        isBucketCreated = True
    except Exception as E:
        print(E)
    return isBucketCreated
def creareLifeCycle(bucketName):
    print(f"Creating LifecycleConfiguration for {bucketName}")
    response = s3.put_bucket_lifecycle(
            Bucket=bucketName,
            LifecycleConfiguration={
                'Rules': [
                    {
                        
                        'ID': 'MoveToGlacier',
                        'Prefix': '/',
                        'Status': 'Enabled',
                        'Transition': {
                            'Days': 30,
                            'StorageClass': 'GLACIER'
                        },
                        'NoncurrentVersionTransition': {
                            'NoncurrentDays': 30,
                            'StorageClass': 'GLACIER'
                        }
                    },
                ]
            }
        )
    print(response)

now = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
bucketName = "ramratan-"+now
print(bucketName)
Check = createBucket(bucketName)
print(Check)
if Check ==True:
    creareLifeCycle(bucketName)
