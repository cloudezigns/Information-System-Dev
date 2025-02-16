from flask import request, jsonify
from app.models import FinancialGoal
from app.extensions import db
from flask_jwt_extended import jwt_required, get_jwt_identity
from . import goals_bp

@goals_bp.route('/api/goals', methods=['POST'])
@jwt_required()
def add_goal():
    # Add goal logic
    ...

@goals_bp.route('/api/goals', methods=['GET'])
@jwt_required()
def get_goals():
    # Get goals logic
    ...
