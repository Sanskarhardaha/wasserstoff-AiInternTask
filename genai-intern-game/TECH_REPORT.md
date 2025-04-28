# Tech Report

## Caching
Used Redis with 1-hour TTL for seed-guess pairs to reduce LLM calls.

## Linked List
Implemented with Python `deque` limited to 50 elements to prevent memory bloat.

## Concurrency
Handled with FastAPI + Uvicorn (async I/O). Rate limiting can be added via middleware.

## Game Logic
Avoids duplicate guesses by checking deque before accepting new entries.

## New Feature Idea
Add multiplayer mode with session-based game states and score leaderboard.