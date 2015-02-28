""" Application Initialization and Setup """

import os
from flask import Flask

# Create app
app = Flask(__name__)

# Read configuration file
config_path = os.environ.get("CONFIG_PATH", "shopping_list.config.HerokuConfig")
app.config.from_object(config_path)

# Import modules
from . import login
from . import api
from . import views
from . import utils

# Database initialization
from .database import Base, engine
Base.metadata.create_all(engine)