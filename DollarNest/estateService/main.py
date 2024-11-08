# Copyright 2020 gRPC authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import asyncio
import logging
import grpc
from ..generated import estate_pb2
from ..generated import estate_pb2_grpc
from ..common.utils import generateRandomId
from .db import EstateDB

estateDB = EstateDB()

class Estate(estate_pb2_grpc.EstateServicer):
    async def GetAllEstate(
        self,
        request: estate_pb2.EstateData,
        context: grpc.aio.ServicerContext,
    ) -> estate_pb2.EstateList:
        rows = estateDB.getAllEstate()
        if rows is None:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("No estates found.")
            return estate_pb2.EstateList()
        estates = [estate_pb2.EstateData(estateId=row["estateId"], type=row["type"],
                                           area=row["area"], transactionDate=row["transactionDate"], price=row["price"], state=row["state"], residenceName=row["residenceName"]) for row in rows]
        return estate_pb2.EstateList(estates=estates)

    async def GetFilteredEstate (
        self,
        request: estate_pb2.EstateFilter,  # Assume this is the request with filters
        context: grpc.aio.ServicerContext,
    ) -> estate_pb2.EstateList:
        # Extract filter parameters from the request
        state = request.state if request.state else None
        residence_name = request.residenceName if request.residenceName else None
        estate_type = request.type if request.type else None

        # Check if date range is provided
        if request.startTransactionDate and request.endTransactionDate:
            date_range = (request.startTransactionDate, request.endTransactionDate)
        else:
            date_range = None

        # Check if price range is provided
        if request.minPrice and request.maxPrice:
            price_range = (request.minPrice, request.maxPrice)
        else:
            price_range = None

        # Call getEstate with dynamic filters
        rows = estateDB.getEstate(state=state, residenceName=residence_name, estate_type=estate_type,
                                    date_range=date_range, price_range=price_range)
        
        if rows is None:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("No estates found.")
            return estate_pb2.EstateList()
        
        # Build the response
        estates = [
            estate_pb2.EstateData(
                estateId=row["estateId"],
                type=row["type"],
                area=row["area"],
                transactionDate=row["transactionDate"],
                price=row["price"],
                state=row["state"],
                residenceName=row["residenceName"]
            )
            for row in rows
        ]
        
        return estate_pb2.EstateList(estates=estates)

    async def CreateEstate(
                self,
                request: estate_pb2.EstateData,
                context: grpc.aio.ServicerContext,
            ) -> estate_pb2.EstateData:
                newEstateId = generateRandomId()
                print(f"GRPC Server: {request}")
                estate = estateDB.createEstate((newEstateId, request.type, request.state, request.area, request.price, request.transactionDate, request.residenceName))
                if estate is None:
                    context.set_code(grpc.StatusCode.INTERNAL)
                    context.set_details("Estate creation failed or error occured.")
                    return estate_pb2.EstateData()
                return estate_pb2.EstateData(estateId=newEstateId, type=request.type, state=request.state, area=request.area, transactionDate=request.transactionDate, price=request.price, residenceName=request.residenceName)

    async def UpdateEstate(self, request: estate_pb2.EstateData, context: grpc.aio.ServicerContext) -> estate_pb2.EstateData:
        updated = estateDB.updateEstate(
            {"price": request.price, "estateId": request.estateId, "state": request.state, "area": request.area, "type": request.type, "transactionDate": request.transactionDate, "residenceName": request.residenceName}
        )
        if not updated:
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details("Estate update failed or error occured.")
            return estate_pb2.EstateData()
        return estate_pb2.EstateData(estateId=request.estateId)

async def serve() -> None:
    server = grpc.aio.server()
    estate_pb2_grpc.add_EstateServicer_to_server(Estate(), server)
    listen_addr = "[::]:50052"
    server.add_insecure_port(listen_addr)
    logging.info("Starting server on %s", listen_addr)
    await server.start()
    await server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(serve())
