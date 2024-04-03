import json
import boto3


def lambda_handler(event, context):
    # Get user information from the event
    username = event['username']
    user_pool_id = event['user_pool_id']

    # Confirm the user's account
    cognito_client = context
    try:
        response = cognito_client.admin_confirm_sign_up(
            UserPoolId=user_pool_id,
            Username=username
        )
        print("User confirmed successfully:", response)
        return event
    except Exception as e:
        print("Error confirming user:", e)
        raise e
