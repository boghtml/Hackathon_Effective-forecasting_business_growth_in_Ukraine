import os

class Config:
    SECRET_KEY = os.urandom(24)
    UPLOAD_FOLDER = 'app/static/uploads'
