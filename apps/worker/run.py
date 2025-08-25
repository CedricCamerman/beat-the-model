import os, time, redis

REDIS_URL = os.getenv("REDIS_URL", "redis://cache:6379/0")
r = redis.from_url(REDIS_URL, decode_responses=True)

def main():
    print("Worker booted. Connected to Redis:", r.ping())
    while True:
        # later: pull jobs from a queue and process
        time.sleep(5)

if __name__ == "__main__":
    main()
