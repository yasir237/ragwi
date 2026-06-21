from fastapi import FastAPI
from routes import base, data, nlp
from helpers.config import get_settings

app = FastAPI()

app.include_router(base.base_router)
app.include_router(data.router)
app.include_router(nlp.router)
