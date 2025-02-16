from flask import request, jsonify
from app.models import User
from app.extensions import db
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from . import auth_bp

@auth_bp.route('/api/register', methods=['POST'])
def register():
    # Registration logic
    ...

@auth_bp.route('/api/login', methods=['POST'])
def login():
    # Login logic
    ...

@auth_bp.route('/api/user/profile', methods=['GET'])
@jwt_required()
def profile():
    # Profile logic
    ...
