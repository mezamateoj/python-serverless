from fastapi import APIRouter
from pydantic import BaseModel
from api.v1.endpoints.agent import Agent

router = APIRouter()
class Item(BaseModel):
    url: str

@router.get("/")
async def testing_child_resource():
    return {"message": "Try /api/v1/url/ and pass a job url"}


@router.post("/url/")
async def create_job(item: Item):
    agent = Agent(url=item.url)
    return {"message": "Site visited!", 'result': agent.result_query()}