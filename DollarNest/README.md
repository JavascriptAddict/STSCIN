## Project Root
- DollarNest folder is the project/package root
- To run any modules within, start from outside the root folder

## Create virtual environment
```shell
cd .\DollarNest\
python -m venv venv
cd ..
```
#### Activate the Virtual Environment
- .\DollarNest\myenv\Scripts\activate

## Install Dependencies
```sh
.\myenv\Scripts\activate
pip install -r requirements.txt
```
### Run the codes in 2 separate cmd all in virtual environment
- Run as a module from package 
- python -m DollarNest.accountService.main
- python -m DollarNest.estateService.main

### Run API Gateway in a separate powershell in virtual environment
- uvicorn DollarNest.apiGateway.main:app --host 0.0.0.0 --port 80

#### Codes for generating pb2 files
From inside the DollarNest folder, invoke this code and change trip to whatever you're generating
```sh
python -m grpc_tools.protoc -I protos --python_out=./generated --pyi_out=./generated --grpc_python_out=./generated protos/estate.proto
```

## Replace API Key
- Replace API key anywhere that has "[API_KEY_HERE]"