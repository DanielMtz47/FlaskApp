from flask import Flask 

app = Flask(__name__)

from FlaskApp import routes
from FlaskApp import apis

