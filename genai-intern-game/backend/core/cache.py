import redis
import os

redis_client = redis.Redis(host=os.getenv("REDIS_HOST", "redis"), port=6379, db=0)

def get_cached_verdict(key):
    result = redis_client.get(key)
    return result.decode() if result else None

def set_cached_verdict(key, verdict):
    redis_client.set(key, verdict, ex=3600)