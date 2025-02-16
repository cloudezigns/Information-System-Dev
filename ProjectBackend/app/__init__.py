from flask import Flask
from .extensions import db, jwt
from .auth import auth_bp
from .expenses import expenses_bp
from .budgets import budgets_bp
from .goals import goals_bp
from .bills import bills_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    # Initialize extensions
    db.init_app(app)
    jwt.init_app(app)

    # Register blueprints
    app.register_blueprint(auth_bp)
    app.register_blueprint(expenses_bp)
    app.register_blueprint(budgets_bp)
    app.register_blueprint(goals_bp)
    app.register_blueprint(bills_bp)

    return app
