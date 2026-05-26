# main.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.routes.product_routes import router as product_router
from db.database import Base, engine
from db.init_db import seed_database
from exceptions.custom_exceptions import ResourceNotFoundException
from core.exception_handler import (
    resource_not_found_exception_handler
)
from middleware.logging_middleware import (
    logging_middleware
)
from core.logging_config import setup_logging
import logging
from contextlib import asynccontextmanager


# ---------------- LOGGING ----------------
setup_logging()
logger = logging.getLogger(__name__)


# ---------------- LIFESPAN ----------------
@asynccontextmanager
async def lifespan(app: FastAPI):

    logger.info(
        "Starting FastAPI application"
    )

    Base.metadata.create_all(
        bind=engine
    )

    seed_database()

    yield

    logger.info(
        "Shutting down FastAPI application"
    )
    

# ---------------- FASTAPI APP ----------------
app = FastAPI(
    title="FastAPI Demo",
    lifespan=lifespan
)


# ---------------- MIDDLEWARE ----------------    
app.middleware("http")(logging_middleware)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],    # allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ---------------- EXCEPTION HANDLERS ----------------
# Register global exception handler
app.add_exception_handler(
    ResourceNotFoundException,
    resource_not_found_exception_handler
)


# ---------------- ROUTES ----------------
@app.get("/api/v1/health")
def health_check():
    logger.info("Health check endpoint called")
    return {"status": "ok"}

app.include_router(product_router)


## Run
# uvicorn main:app --reload
# http://127.0.0.1:8000/docs
