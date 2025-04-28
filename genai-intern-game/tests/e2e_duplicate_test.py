import requests

def test_duplicate_guess():
    base_url = "http://localhost:8000/api/v1/game/guess"
    seed = "Rock"
    guess = "Paper"

    data = {"seed": seed, "guess": guess}
    first = requests.post(base_url, json=data)
    second = requests.post(base_url, json=data)

    assert first.status_code == 200
    assert second.json().get("game_over") == True