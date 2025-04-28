from backend.core.ai_client import query_ai
from backend.core.cache import get_cached_verdict, set_cached_verdict
from backend.db.models import update_guess_counter, check_duplicate, add_guess_to_list

async def process_guess(seed, guess, persona):
    cache_key = f"{seed.lower()}:{guess.lower()}"
    verdict = get_cached_verdict(cache_key)

    if verdict is None:
        verdict = await query_ai(seed, guess, persona)
        set_cached_verdict(cache_key, verdict)

    if verdict.lower() == "yes":
        if check_duplicate(guess):
            return {"game_over": True, "message": f"'{guess}' already used!"}
        count = update_guess_counter(guess)
        add_guess_to_list(guess)
        return {
            "message": f"✅ Nice! '{guess}' beats '{seed}'. Guessed {count} times before.",
            "score_increment": 1,
            "game_over": False
        }

    return {
        "message": f"❌ Nope! '{guess}' does not beat '{seed}'",
        "score_increment": 0,
        "game_over": False
    }