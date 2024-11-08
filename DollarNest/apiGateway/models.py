from pydantic import BaseModel


class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    userId: str
    
class Account(BaseModel):
    name: str 
    
class AccountCreation(Account):
    password: str
    username: str
    
class AccountUpdate(Account):
    password: str
    
class AccountResponse(Account):
    userId: str
    password: str
    accountStatus: str

class Estate(BaseModel):
    state: str
    area: str
    type: str
    transactionDate: str
    price: float
    residenceName: str
    
class EstateResponse(Estate):
    estateId: str