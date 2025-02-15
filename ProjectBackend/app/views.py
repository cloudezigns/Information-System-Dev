from flask import Blueprint, request, jsonify
from app import db
from app.models import User
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/api/register', methods=['POST'])
def register():
    data = request.get_json()
    if User.query.filter_by(username=data['username']).first():
        return jsonify({'message': 'User already exists'}), 400
    new_user = User(username=data['username'])
    new_user.set_password(data['password'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'User registered successfully'}), 201

@auth_bp.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User.query.filter_by(username=data['username']).first()
    if user and user.check_password(data['password']):
        access_token = create_access_token(identity=user.id)
        return jsonify({'access_token': access_token}), 200
    return jsonify({'message': 'Invalid credentials'}), 401

@auth_bp.route('/api/user/profile', methods=['GET'])
@jwt_required()
def profile():
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    return jsonify({
        'id': user.id,
        'username': user.username
    }), 200
