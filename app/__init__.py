from flask import Flask
from config import Config
from flask_cors import CORS

# instanciating app in Flask class
app = Flask(__name__)

app.config.from_object(Config)

from .models import db
db._init_(app)

CORS(app)

# this line of code - directs the flask app to routes for web routes
from . import routes

from . import models




# new directory for organization
from .auth.routes import auth
app.register_blueprint(auth)

from .api.routes import api
app.register_blueprint(api)