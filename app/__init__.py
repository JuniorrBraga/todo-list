from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:jo7422463158@A@localhost:5432/todoflaskdb'
    db.init_app(app)
    
    from .routes import main
    app.register_blueprint(main)
    
    return app
