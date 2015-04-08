import os
import logging
import redis
from flask import Flask

app = Flask(__name__)
db = redis.from_url(os.environ['REDISCLOUD_URL'])

logging.basicConfig(level=logging.DEBUG)

@app.route('/')
def hello():
    logging.info("saying hello")
    name = db.get('name') or 'World'
    return 'Hello {}!'.format(name)

@app.route('/setname/<name>')
def setname(name):
    db.set('name', name)
    return 'Name updated.'
