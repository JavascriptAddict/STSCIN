from ..generated import account_pb2_grpc, account_pb2, estate_pb2, estate_pb2_grpc
from .models import AccountCreation, AccountUpdate, Estate
from fastapi import HTTPException
from dotenv import load_dotenv
from typing import Optional
import grpc
import os

load_dotenv()

ACCOUNT_SERVICE_ADDRESS = os.getenv('ACCOUNT_SERVICE_ADDRESS') 
ESTATE_SERVICE_ADDRESS = os.getenv('ESTATE_SERVICE_ADDRESS') 

async def getAccountById(accountId: str) -> account_pb2.AccountResponse:
    async with grpc.aio.insecure_channel(ACCOUNT_SERVICE_ADDRESS) as channel:
        stub = account_pb2_grpc.AccountStub(channel)
        try:
            response = await stub.GetAccountById(account_pb2.AccountRequestById(userId=accountId))
            return response
        except grpc.aio.AioRpcError as e:
            raise HTTPException(status_code=404, detail=f"Error: {e.details()}")


async def getAccountByUsername(accountUsername: str) -> account_pb2.AccountResponse:
    async with grpc.aio.insecure_channel(ACCOUNT_SERVICE_ADDRESS) as channel:
        stub = account_pb2_grpc.AccountStub(channel)
        try:
            response = await stub.GetAccountByUsername(account_pb2.AccountRequestByUsername(username=accountUsername))
            return response
        except grpc.aio.AioRpcError as e:
            raise HTTPException(status_code=404, detail=f"Error: {e.details()}")
        
async def createAccount(account: AccountCreation) -> account_pb2.AccountResponse:
    async with grpc.aio.insecure_channel(ACCOUNT_SERVICE_ADDRESS) as channel:
        stub = account_pb2_grpc.AccountStub(channel)
        try:
            response = await stub.CreateAccount(account_pb2.CreateAccountRequest(
                name=account.name, 
                username=account.username,
                password=account.password
            ))
            return response
        except grpc.aio.AioRpcError as e:
            raise HTTPException(status_code=500, detail=f"Error: {e.details()}")

async def updateAccount(accountId: str, account: AccountUpdate) -> account_pb2.AccountResponse:
    async with grpc.aio.insecure_channel(ACCOUNT_SERVICE_ADDRESS) as channel:
        stub = account_pb2_grpc.AccountStub(channel)
        try:
            response = await stub.UpdateAccount(account_pb2.UpdateAccountRequest(
                userId=accountId,
                name=account.name,
                password=account.password
            ))
            return response
        except grpc.aio.AioRpcError as e:
            raise HTTPException(status_code=500, detail=f"Error: {e.details()}")

                      
async def deleteAccount(accountId: str) -> None:
    async with grpc.aio.insecure_channel(ACCOUNT_SERVICE_ADDRESS) as channel:
        stub = account_pb2_grpc.AccountStub(channel)
        try:
            response = await stub.DeleteAccount(account_pb2.AccountRequestById(userId=accountId))
            return response
        except grpc.aio.AioRpcError as e:
            raise HTTPException(status_code=500, detail=f"Error: {e.details()}")


async def getEstate() -> estate_pb2.EstateList:
    async with grpc.aio.insecure_channel(ESTATE_SERVICE_ADDRESS) as channel:
        stub = estate_pb2_grpc.EstateStub(channel)
        try:
            response = await stub.GetAllEstate(estate_pb2.EstateData())
            return response
        except grpc.aio.AioRpcError as e:
            raise HTTPException(status_code=404, detail=f"Error: {e.details()}")

async def getFilteredEstate(
    state: Optional[str] = None,
    residenceName: Optional[str] = None,
    estate_type: Optional[str] = None,
    startTransactionDate: Optional[str] = None,
    endTransactionDate: Optional[str] = None,
    minPrice: Optional[float] = None,
    maxPrice: Optional[float] = None
) -> estate_pb2.EstateList:
    async with grpc.aio.insecure_channel(ESTATE_SERVICE_ADDRESS) as channel:
        stub = estate_pb2_grpc.EstateStub(channel)
        
        # Construct the request with optional filters
        request = estate_pb2.EstateFilter(
            state=state or "",
            residenceName=residenceName or "",
            type=estate_type or "",
            startTransactionDate=startTransactionDate or "",
            endTransactionDate=endTransactionDate or "",
            minPrice=minPrice if minPrice is not None else 0.0,
            maxPrice=maxPrice if maxPrice is not None else 0.0,
        )
        
        try:
            # Call the GetFilteredEstate RPC with the constructed request
            response = await stub.GetFilteredEstate(request)
            return response
        except grpc.aio.AioRpcError as e:
            raise HTTPException(status_code=404, detail=f"Error: {e.details()}")

async def createEstate(estate: Estate) -> estate_pb2.EstateData:
    async with grpc.aio.insecure_channel(ESTATE_SERVICE_ADDRESS) as channel:
        stub = estate_pb2_grpc.EstateStub(channel)
        try:
            response = await stub.CreateEstate(estate_pb2.EstateData(state=estate.state, area=estate.area, type=estate.type, transactionDate=estate.transactionDate, price=estate.price, residenceName=estate.residenceName))
            return response
        except grpc.aio.AioRpcError as e:
            raise HTTPException(status_code=500, detail=f"Error: {e.details()}")

async def updateEstate(estateId: str, estate: Estate) -> estate_pb2.EstateData:
    async with grpc.aio.insecure_channel(ESTATE_SERVICE_ADDRESS) as channel:
        stub = estate_pb2_grpc.EstateStub(channel)
        try:
            response = await stub.UpdateEstate(estate_pb2.EstateData(estateId=estateId,state=estate.state, area=estate.area, type=estate.type, transactionDate=estate.transactionDate, price=estate.price))
            return response
        except grpc.aio.AioRpcError as e:
            raise HTTPException(status_code=500, detail=f"Error: {e.details()}")
