from boto3 import client
from fastapi import HTTPException

from src.models.user_models import UserRegistration, UserLogin
from config import env
from src.utils.lamba_user_verification import lambda_handler
from src.utils.utils import calculate_secret_hash


class UserView:
    # AWS Cognito configurations
    cognito_client = client('cognito-idp', region_name=env.cognito_client.get('aws_region'))

    def register_user(self,user_info: UserRegistration):
        try:
            cognito_client_id=env.cognito_client.get('cognito_client_id')
            secret_hash = calculate_secret_hash(cognito_client_id,
                                                env.cognito_client.get('cognito_client_secret'),
                                                user_info.username)

            response = self.cognito_client.sign_up(
                ClientId=cognito_client_id,
                Username=user_info.username,
                Password=user_info.password,

                UserAttributes=[
                    {'Name': 'email', 'Value': user_info.email},
                    {'Name': 'name', 'Value': user_info.name}

                ],
                SecretHash=secret_hash

            )

            return response
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))

    def authenticate_user(self,login_info: UserLogin):
        try:
            secret_hash = calculate_secret_hash(env.cognito_client.get('cognito_client_id'),
                                                env.cognito_client.get('cognito_client_secret'),
                                                login_info.username)

            response = self.cognito_client.initiate_auth(
                ClientId=env.cognito_client.get('cognito_client_id'),
                AuthFlow='USER_PASSWORD_AUTH',
                AuthParameters={
                    'USERNAME': login_info.username,
                    'PASSWORD': login_info.password,
                    'SECRET_HASH': secret_hash

                }
            )
            return response
        except Exception as e:
            raise HTTPException(status_code=401, detail=str(e))