import redis

redis_host = 'localhost'
redis_port = 6379


def redis_string():
    try:
        r = redis.StrictRedis(
            host=redis_host, port=redis_port, decode_responses=True)
        r.set("message", "Hello, world!")
        msg = r.get("message")
        print(msg)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    redis_string()

# r = redis.Redis(
#     host='teste-redis-aws.tqfong.ng.0001.sae1.cache.amazonaws.com',
#     port=6379, db=0,
#     ssl=True,
#     ssl_cert_reqs=None)
