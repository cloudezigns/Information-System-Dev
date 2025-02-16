from flask import request, jsonify
from app.models import BillReminder
from app.extensions import db
from flask_jwt_extended import jwt_required, get_jwt_identity
from . import bills_bp

@bills_bp.route('/api/bills', methods=['POST'])
@jwt_required()
def add_bill():
    # Add bill logic
    ...

@bills_bp.route('/api/bills', methods=['GET'])
@jwt_required()
def get_bills():
    # Get bills logic
    ...
