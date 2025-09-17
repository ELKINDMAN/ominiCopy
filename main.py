from fastapi import FastAPI, HTTPException, Request, Response
from datetime import datetime
from typing import Any
from random import randint


app = FastAPI(root_path="/api/v1")

@app.get("/")
async def root():
    return {"message": "Hello Fast"}

data : Any = [
    {
        "campaign_id": 1,
     "name": "Welcome to Store",
     "due_date": datetime.now(),
     "created_at": datetime.now()
     },
    {
        "campaign_id": 2,
     "name": "Black Friday",
     "due_date": datetime.now(),
     "created_at": datetime.now()
     },
      {
        "campaign_id": 3,
     "name": "Summer Launch Friday",
     "due_date": datetime.now(),
     "created_at": datetime.now()
     },
]

"""
Campaigns
- campaign_id
- name
- due_date
- created_at
"""

@app.get("/campaigns")
async def read_campaigns():
    return {"Campaigns": data}

@app.get("/campaigns/{id}")
async def read_campaign(id: int):
    for campaign in data:
        if campaign.get("campaign_id") == id:
            return {"campaign": campaign}
    raise HTTPException(status_code=404)
@app.post("/campaigns")
async def create_campaign(body: dict[str, Any]):

    new = {
        "campaign_id": randint(4, 100),
        "name": body.get("name"),
        "due_date": body.get("due_date"),
        "created_at": datetime.now()
    }

    data.append(new)
    return {"campaign": new}
@app.put("/campaigns/{id}")
async def update_campaign(id: int, body: dict[str, Any]):
    for index, campaign in enumerate(data):
        if campaign.get("campaign_id") == id:

            update : Any = {
                "campaign_id": id,
                "name": body.get("name"),
                "due_date": body.get("due_date"),
                "created_at": campaign.get("created_at")                
            }

            data[index] = update
            return {"campaign": update}
    raise HTTPException(status_code=404)

@app.delete("/campaigns/{id}")
async def delete_campaign(id: int):

    for index, campaign in enumerate(data):
        if campaign.get("campaign_id") == id:
            data.pop(index)
            return Response(status_code=204)
    raise HTTPException(status_code=404)