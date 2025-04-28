from fastapi import FastAPI
from backend.api.routes import game_router

app = FastAPI(title="GenAI Guessing Game")

app.include_router(game_router, prefix="/api/v1/game")