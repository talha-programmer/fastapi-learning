from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

# SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"

# For Sync
SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:password@localhost/fastapi"  

ASYNC_SQLALCHEMY_DATABASE_URL = "mysql+aiomysql://root:password@localhost/fastapi"

# future=True for using async functionality
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, future=True
)

async_engine = create_async_engine(
    ASYNC_SQLALCHEMY_DATABASE_URL
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine, future=True)

AsyncSessionLocal = sessionmaker(
    async_engine, class_=AsyncSession, expire_on_commit=False
)

Base = declarative_base()

# DB Utilities
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# DB Utilities
async def get_async_db():
    async with AsyncSessionLocal() as db:
        yield db
        await db.commit()