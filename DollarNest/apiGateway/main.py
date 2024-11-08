from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.staticfiles import StaticFiles
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.middleware.cors import CORSMiddleware
from .auth import createAccessToken, verifyPassword
from .gRPCHandler import getAccountByUsername
from .api.account import account
from .api.estate import estate

from .models import Token
from datetime import timedelta
import os 

TOKEN_EXPIRE_MINUTES = 30

app = FastAPI()

currentPath = os.path.dirname(os.path.abspath(__file__))

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Set to all just for ease of development. In actual use, it should be limited to specific ones
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/token", response_model=Token)
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = await getAccountByUsername(form_data.username)
    if not user or not verifyPassword(form_data.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    accessTokenExpiry = timedelta(minutes=TOKEN_EXPIRE_MINUTES)
    accessToken = createAccessToken(data={"sub": user.userId}, expireDelta=accessTokenExpiry)
    return {"access_token": accessToken, "token_type": "bearer"}

app.include_router(account)
app.include_router(estate)
app.mount("/", StaticFiles(directory=currentPath + "/public", html = True), name="static")