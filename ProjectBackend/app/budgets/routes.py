from flask import request, jsonify
from app.models import Budget
from app.extensions import db
from flask_jwt_extended import jwt_required, get_jwt_identity
from . import budgets_bp

@budgets_bp.route('/api/budgets', methods=['POST'])
@jwt_required()
def add_budget():
    # Add budget logic
    ...

@budgets_bp.route('/api/budgets', methods=['GET'])
@jwt_required()
def get_budgets():
    # Get budgets logic
    ...
