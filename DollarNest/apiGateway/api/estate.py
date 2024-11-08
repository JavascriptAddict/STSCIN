from fastapi import APIRouter, Depends, HTTPException, Query
from ..gRPCHandler import getEstate, createEstate, updateEstate, getFilteredEstate
from google.protobuf.json_format import MessageToDict
from ..models import AccountResponse, Estate
from ..auth import getCurrentUser

estate = APIRouter()

@estate.get("/estate")
async def get_estate():
    estates = MessageToDict(await getEstate())
    return {"message": "Estates retrieved", "data": estates}

@estate.get("/estate/filtered")
async def get_estate(
    state: str = Query(None),
    residenceName: str = Query(None),
    estate_type: str = Query(None, alias="type"),
    startTransactionDate: str = Query(None),
    endTransactionDate: str = Query(None),
    minPrice: float = Query(None),
    maxPrice: float = Query(None)
):
    try:
        # Pass query parameters to the getEstate function
        estates = MessageToDict(
            await getFilteredEstate(
                state=state,
                residenceName=residenceName,
                estate_type=estate_type,
                startTransactionDate=startTransactionDate,
                endTransactionDate=endTransactionDate,
                minPrice=minPrice,
                maxPrice=maxPrice
            )
        )
        return {"message": "Estates retrieved", "data": estates}
    except HTTPException as e:
        return {"message": str(e.detail)}
    
@estate.post("/estate/create") 
async def create_estate(estate: Estate): 
    print(f"API: {estate.residenceName}")
    newEstate = await createEstate(estate) 
    if newEstate is None:
        raise HTTPException(status_code=500, detail="Error occured")
    return {"message": "Estate created", "data": MessageToDict(newEstate)}

@estate.put("/estate/update")
async def update_account_embedding(estateId: str, estate: Estate, currentUser: AccountResponse = Depends(getCurrentUser)):
    response = await updateEstate(estateId, estate)
    if response is None:
        raise HTTPException(status_code=500, detail="Error occured")
    return {"message": "Estate updated", "data": MessageToDict(response)}