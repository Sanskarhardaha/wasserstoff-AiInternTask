from fastapi import APIRouter, Request, HTTPException
from backend.core.game_logic import process_guess
from backend.core.moderation import check_profanity

game_router = APIRouter()

@game_router.post("/guess")
async def make_guess(request: Request):
    data = await request.json()
    seed = data.get("seed")
    guess = data.get("guess")
    persona = data.get("persona", "serious")

    if check_profanity(guess):
        raise HTTPException(status_code=400, detail="Inappropriate content detected")

    result = await process_guess(seed, guess, persona)
    return result