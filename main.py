from fastapi import FastAPI
from scripts.handlers.handler import router as file_router
from scripts.database.database import create_db_and_tables

app = FastAPI(root_path="/plugin/project-139/fast-plugin2/api")

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

app.include_router(file_router)
