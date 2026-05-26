# main.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.routes.product_routes import router as product_router
from db.database import Base, engine
from db.init_db import seed_database

Base.metadata.create_all(bind=engine)
seed_database()

app = FastAPI(
    title="FastAPI Demo"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],    # allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/v1/health")
def health_check():
    return {"status": "ok"}

app.include_router(product_router)


## Run
# uvicorn main:app --reload
# http://127.0.0.1:8000/docs