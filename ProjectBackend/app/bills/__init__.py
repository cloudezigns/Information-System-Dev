from flask import Blueprint

bills_bp = Blueprint('bills', __name__)

from . import routes
