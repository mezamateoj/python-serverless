from fastapi import APIRouter
from pydantic import BaseModel
from api.v1.endpoints.agent import Agent

router = APIRouter()
class Item(BaseModel):
    url: str

@router.get("/")
async def testing_child_resource():
    return {"message": "Hi There from api/v1. try /api/v1/url/ and pass a job url as a json body"}


@router.post("/url/")
async def create_job(item: Item):
    agent = Agent(url=item.url)
    return {"message": "Site visited successfully!", 'result': agent.result_query()}