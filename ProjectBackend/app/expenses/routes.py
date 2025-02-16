from flask import request, jsonify
from app.models import Expense
from app.extensions import db
from flask_jwt_extended import jwt_required, get_jwt_identity
from . import expenses_bp
from datetime import datetime

@expenses_bp.route('/api/expenses', methods=['POST'])
@jwt_required()
def add_expense():
    # Add expense logic
    ...

@expenses_bp.route('/api/expenses', methods=['GET'])
@jwt_required()
def get_expenses():
    # Get expenses logic
    ...
