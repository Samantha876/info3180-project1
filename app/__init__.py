from flask import Flask
from .config import Config
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(Config)
#from app import models

db = SQLAlchemy(app)

from app import models,views
