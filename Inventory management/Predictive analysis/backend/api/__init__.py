from flask import Blueprint
from .routes import api_blueprint

# Initialize blueprints
api = Blueprint('api', __name__)