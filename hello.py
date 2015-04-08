import os
import logging
from flask import Flask

app = Flask(__name__)

logging.basicConfig(level=logging.DEBUG)

@app.route('/')
def hello():
    logging.info("saying hello")
    name = os.environ.get('NAME', 'World')
    return 'Hello {}!'.format(name)
