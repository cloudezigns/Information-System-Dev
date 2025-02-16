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
"""Add Expense Endpoint: Adds a new expense."""
@bp.route('/api/expenses', methods=['POST'])
@jwt_required()
def add_expense():
    user_id = get_jwt_identity()
    data = request.get_json()
    new_expense = Expense(
        user_id=user_id,
        amount=data['amount'],
        category=data['category'],
        description=data.get('description', ''),
        date=data.get('date', datetime.utcnow())
    )
    db.session.add(new_expense)
    db.session.commit()
    return jsonify({'message': 'Expense added successfully'}), 201

"""Get Expenses Endpoint: Retrieves all expenses for the authenticated user."""
@bp.route('/api/expenses', methods=['GET'])
@jwt_required()
def get_expenses():
    user_id = get_jwt_identity()
    expenses = Expense.query.filter_by(user_id=user_id).all()
    return jsonify([{
        'id': exp.id,
        'amount': exp.amount,
        'category': exp.category,
        'description': exp.description,
        'date': exp.date
    } for exp in expenses]), 200

"""Add Budget Endpoint: Adds a new budget."""
@bp.route('/api/budgets', methods=['POST'])
@jwt_required()
def add_budget():
    user_id = get_jwt_identity()
    data = request.get_json()
    new_budget = Budget(
        user_id=user_id,
        category=data['category'],
        budgeted_amount=data['budgeted_amount'],
        start_date=data['start_date'],
        end_date=data['end_date']
    )
    db.session.add(new_budget)
    db.session.commit()
    return jsonify({'message': 'Budget added successfully'}), 201

"""Get Budgets Endpoint: Retrieves all budgets for the authenticated user."""
@bp.route('/api/budgets', methods=['GET'])
@jwt_required()
def get_budgets():
    user_id = get_jwt_identity()
    budgets = Budget.query.filter_by(user_id=user_id).all()
    return jsonify([{
        'id': bud.id,
        'category': bud.category,
        'budgeted_amount': bud.budgeted_amount,
        'start_date': bud.start_date,
        'end_date': bud.end_date
    } for bud in budgets]), 200

"""Add Financial Goal Endpoint: Adds a new financial goal."""
@bp.route('/api/goals', methods=['POST'])
@jwt_required()
def add_goal():
    user_id = get_jwt_identity()
    data = request.get_json()
    new_goal = FinancialGoal(
        user_id=user_id,
        goal_name=data['goal_name'],
        target_amount=data['target_amount'],
        current_amount=data.get('current_amount', 0.0),
        deadline=data['deadline']
    )
    db.session.add(new_goal)
    db.session.commit()
    return jsonify({'message': 'Financial goal added successfully'}), 201

"""Get Financial Goals Endpoint: Retrieves all financial goals for the authenticated user."""
@bp.route('/api/goals', methods=['GET'])
@jwt_required()
def get_goals():
    user_id = get_jwt_identity()
    goals = FinancialGoal.query.filter_by(user_id=user_id).all()
    return jsonify([{
        'id': goal.id,
        'goal_name': goal.goal_name,
        'target_amount': goal.target_amount,
        'current_amount': goal.current_amount,
        'deadline': goal.deadline
    } for goal in goals]), 200

"""Add Bill Reminder Endpoint: Adds a new bill reminder."""
@bp.route('/api/bills', methods=['POST'])
@jwt_required()
def add_bill():
    user_id = get_jwt_identity()
    data = request.get_json()
    new_bill = BillReminder(
        user_id=user_id,
        bill_name=data['bill_name'],
        amount=data['amount'],
        due_date=data['due_date'],
        paid=data.get('paid', False)
    )
    db.session.add(new_bill)
    db.session.commit()
    return jsonify({'message': 'Bill reminder added successfully'}), 201

"""Get Bill Reminders Endpoint: Retrieves all bill reminders for the authenticated user."""
@bp.route('/api/bills', methods=['GET'])
@jwt_required()
def get_bills():
    user_id = get_jwt_identity()
    bills = BillReminder.query.filter_by(user_id=user_id).all()
    return jsonify([{
        'id': bill.id,
        'bill_name': bill.bill_name,
        'amount': bill.amount,
        'due_date': bill.due_date,
        'paid': bill.paid
    } for bill in bills]), 200














