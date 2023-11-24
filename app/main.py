from fastapi import FastAPI
from mangum import Mangum
from api.v1.api import router as api_router

app = FastAPI(title='Serverless Lambda FastAPI')

@app.get("/",  tags=["Entry Point"])
def main_endpoint_test():
    return {"message": "Welcome to the Serverless Lambda FastAPI ai web-crawler. try /api/v1"}

app.include_router(api_router, prefix="/api/v1")
# to make it work with Amazon Lambda, we create a handler object
handler = Mangum(app=app)