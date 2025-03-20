import boto3
from datetime import datetime, timezone
import json

def get_iam_client():
    return boto3.client('iam')

def check_unused_users(days_threshold=90):
    iam = get_iam_client()
    
    try:
        # Get credential report
        iam.generate_credential_report()
        response = iam.get_credential_report()
        credentials = response['Content'].decode('utf-8').split('\n')
        
        # Skip the header row
        headers = credentials[0].split(',')
        print(headers)
        users = credentials[1:]
        
        current_time = datetime.now(timezone.utc)
        
        for user in users:
            user_data = dict(zip(headers, user.split(',')))
            username = user_data['user']
            password_enabled = user_data['password_enabled']
            # Skip root account
            if username == '<root_account>':
                continue
                
            password_last_used = user_data.get('password_last_used', 'N/A')
            access_key_1_last_used = user_data.get('access_key_1_last_used_date', 'N/A')
            access_key_2_last_used = user_data.get('access_key_2_last_used_date', 'N/A')
            
            is_unused = True
            
            # Check password usage
            if password_last_used != 'N/A' and password_last_used != 'no_information':
                last_used = datetime.fromisoformat(password_last_used.replace('Z', '+00:00'))
                days_since_use = (current_time - last_used).days
                if days_since_use < days_threshold:
                    is_unused = False
            
            # Check access key 1 usage
            if access_key_1_last_used != 'N/A' and access_key_1_last_used != 'no_information':
                last_used = datetime.fromisoformat(access_key_1_last_used.replace('Z', '+00:00'))
                days_since_use = (current_time - last_used).days
                if days_since_use < days_threshold:
                    is_unused = False
            
            # Check access key 2 usage
            if access_key_2_last_used != 'N/A' and access_key_2_last_used != 'no_information':
                last_used = datetime.fromisoformat(access_key_2_last_used.replace('Z', '+00:00'))
                days_since_use = (current_time - last_used).days
                if days_since_use < days_threshold:
                    is_unused = False
            
            if is_unused:
                print(f"User {username} has been inactive for more than {days_threshold} days")
                # Disable the user by attaching deny policy
                if password_enabled == True:
                    iam.update_login_profile(UserName=username, PasswordResetRequired=True)
                # Deactivate access keys
                try:
                    access_keys = iam.list_access_keys(UserName=username)['AccessKeyMetadata']
                    for key in access_keys:
                        iam.update_access_key(
                            UserName=username,
                            AccessKeyId=key['AccessKeyId'],
                            Status='Inactive'
                        )
                        print(f"Deactivated access key {key['AccessKeyId']} for user {username}")
                except Exception as e:
                    print(f"Error deactivating access keys for {username}: {str(e)}")
    except Exception as e:
        print(f"Error {str(e)}")

def main():
    # Set the threshold for unused days (default 90 days)
    UNUSED_DAYS_THRESHOLD = 90
    
    print(f"Checking for users inactive for more than {UNUSED_DAYS_THRESHOLD} days...")
    check_unused_users(UNUSED_DAYS_THRESHOLD)
    print("Completed checking for unused users")

if __name__ == "__main__":
    main()
