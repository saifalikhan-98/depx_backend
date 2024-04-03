from fastapi import FastAPI
from src.models.user_models import UserRegistration, UserLogin
from src.views.user_view import UserView
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)
@app.post("/register/")
async def register_new_user(user_info: UserRegistration):
    UserView().register_user(user_info)
    return {"message": "User registered successfully"}

@app.post("/login/")
async def login_user(login_info: UserLogin):
    auth_response = UserView().authenticate_user(login_info)
    # Extract access token from the authentication response
    access_token = auth_response['AuthenticationResult']['AccessToken']
    return {"access_token": access_token}
