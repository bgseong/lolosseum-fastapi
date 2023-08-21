import redis



def redis_config():
    try:
        REDIS_HOST = "localhost"
        REDIS_PORT = 6379
        rd = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)
        return rd

    except:
        print("redis connection failure")