from typing import List
from uuid import uuid4
from fastapi import FastAPI

from models import User, Gender, Role

app = FastAPI()

db: List[User] = [
    User(id=uuid4(), 
        first_name = "Varun", 
        last_name = "Rodrigues", 
        gender = Gender.male,
        roles = [Role.admin],
        wallet = 1000
    ),
    User(id=uuid4(), 
        first_name = "Test", 
        last_name = "User1", 
        gender = Gender.female,
        roles = [Role.student, Role.user],
        active = False
    )
]

@app.get("/")
async def root():
    return {"Hello": "mundo"}


@app.get("/api/v1/users")
async def fetch_users():
    return db


'''
Schema
    id
    first_name
    middle_name
    last_name
    gender
    roles
    wallet
    active
'''