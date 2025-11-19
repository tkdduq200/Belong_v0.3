# belong/__init__.py

from flask import Flask
from belong.config import *
from belong.extensions import db, migrate


def create_app():
    app = Flask(__name__)
    app.config.from_object("belong.config")

    # -----------------------
    # Extensions
    # -----------------------
    db.init_app(app)
    migrate.init_app(app, db)

    # -----------------------
    # Models (migrate 인식용)
    # -----------------------
    from belong.models import User, Question, LonelyPrediction

    # -----------------------
    # Blueprints
    # -----------------------
    from belong.views.main_views import bp as main_bp
    from belong.views.auth_views import bp as auth_bp
    from belong.views.question_views import bp as question_bp
    from belong.views.answer_views import bp as answer_bp
    from belong.views.predict_views import bp as predict_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(question_bp)
    app.register_blueprint(answer_bp)
    app.register_blueprint(predict_bp)

    return app
