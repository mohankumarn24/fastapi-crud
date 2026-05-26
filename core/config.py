# config.py

from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")


## Create a `.env` file in project root
# DATABASE_URL=postgresql://postgres:password@localhost:5432/mydb