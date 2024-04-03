import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

class DefaultConfig:
    def __init__(self, *args, **kwargs):
        self.cognito_client = kwargs.get("cognito")


class Development(DefaultConfig):
    def __init__(self):
        cognito={
            "aws_region": os.environ.get("AWS_REGION"),
            "cognito_pool_id": os.environ.get("COGNITO_USER_POOL_ID"),
            "cognito_client_id": os.environ.get("COGNITO_APP_CLIENT_ID"),
            "cognito_client_secret": os.environ.get("COGNITO_APP_CLIENT_SECRET"),
       }

        super().__init__(cognito=cognito)




def __get_enviroment():
    """
        although we can have different env, Im returning Development as default as it is an assignment
    :return:
    """
    return Development()

env = __get_enviroment()