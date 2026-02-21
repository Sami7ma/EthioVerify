from fastapi import FastAPI
from api.routes import router

app = FastAPI(title="Ethio-Verify")

app.include_router(router)
