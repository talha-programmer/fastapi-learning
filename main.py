from fastapi import FastAPI
import api.users as users, courses, sections

from db.db_setup import engine
from db.models import user

# bind all the models to the engine
user.Base.metadata.create_all(bind=engine) 

app = FastAPI(
    title="LMS to Learn FastAPI",
    description="Just a sample LMS",
    version="0.0.2",
    contact={
        "name": "Talha",
        "email": "samplemail@mail.com",
    },
    license_info={
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    },
)

app.include_router(users.router)