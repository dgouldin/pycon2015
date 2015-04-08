import os
from flask import Flask

app = Flask(__name__)

import logging
logging.basicConfig(level=logging.DEBUG)

@app.route('/')
def hello():
    logging.info("saying hello")
    return 'Hello world!'
