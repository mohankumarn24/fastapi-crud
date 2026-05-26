## Setup

1. **Create and activate virtual environment:**
   ```bash
   python -m venv .venv
   Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
   .venv\Scripts\activate
   ```

2. **Install dependencies:**
   ```bash
   pip install fastapi uvicorn sqlalchemy psycopg2-binary python-dotenv pydantic-settings
   ```

3. **PostgreSQL Setup**
   Create database:

   ```sql
   CREATE DATABASE mydb;
   ```

   Create schema:

   ```sql
   CREATE SCHEMA fastapi-crud;
   ```

4. Environment Variables

   Create a `.env` file in project root:

   ```env
   DATABASE_URL=postgresql://postgres:password@localhost:5432/mydb
   ```

5. **Run the application:**
   ```bash
   uvicorn main:app --reload
   ```

6. **Access the API:**
   - API: http://localhost:8000
   - Interactive docs: http://localhost:8000/docs
   - ReDoc: http://localhost:8000/redoc

## Settings
   Create a `.vscode` folder in project root and create `settings.json` file:
   ```
   {
      "files.exclude": {
         "**/__pycache__": true,
         "**/*.pyc": true,
         "**/__init__.py": true
      }
   }
   ```


## Built With

- [FastAPI](https://fastapi.tiangolo.com/) - Modern, fast web framework for building APIs
- [Pydantic](https://pydantic-docs.helpmanual.io/) - Data validation using Python type hints
- [Uvicorn](https://www.uvicorn.org/) - ASGI server implementation