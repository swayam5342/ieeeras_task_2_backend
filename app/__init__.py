from fastapi import FastAPI
from app.routes.home import root

app = FastAPI(title="Book API")
app.include_router(root)