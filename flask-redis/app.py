#import time
#import redis
from flask import Flask
from prometheus_client import start_http_server

if __name__ == "__main__":
    print("running http server on 8010")
    start_http_server(8010)

app = Flask(__name__)

"""
cache = redis.Redis(host='redis', port=6379)


def get_hit_count():
    retries = 5
    while True:
        try:
            return cache.incr('hits')
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)
"""

@app.route('/')
def hello():
    #return "hello to my sample flask app, I have been seen {} times\n".format(get_hit_count())
    return "hello to my sample flask app"
