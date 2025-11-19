# belong/config.py

import os

BASE_DIR = os.path.dirname(__file__)

SQLALCHEMY_DATABASE_URI = f"sqlite:///{os.path.join(BASE_DIR, 'belong.db')}"
SQLALCHEMY_TRACK_MODIFICATIONS = False

SECRET_KEY = "dev-secret-key"
