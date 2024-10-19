from fastapi import FastAPI
from app.database import engine, Base
from app.routers import invoice

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(invoice.router)


@app.get("/")
def read_root():
    return {"msg": "Welcome to MoneyMate"}
