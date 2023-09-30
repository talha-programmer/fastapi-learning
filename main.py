from typing import Optional, List
from fastapi import FastAPI, Path, Query
from pydantic import BaseModel

app = FastAPI(
    title="LMS to Learn FastAPI",
    description="Just a sample LMS",
    version="0.0.1",
    contact={
        "name": "Talha",
        "email": "samplemail@mail.com",
    },
    license_info={
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    },
)

users = []

class User(BaseModel):
    email: str
    is_active: bool
    bio: Optional[str]


@app.get("/users", response_model=List[User])
async def get_users():
    return users



# In the post request we can define path parameters like that: app.post("/users")

@app.post("/users")
async def create_user(user: User):
    users.append(user)
    return "Saved"


@app.get("/users/{id}")
async def get_user(
    id: int = Path(..., description="The ID of the user"),  # ... means it's required. Called epllepsis (Something like that)
    q: str = Query(None, max_length=5)    # None means optional parameter
):      
    return {"user" : users[id], "q": q}