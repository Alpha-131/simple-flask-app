import os

class config():
    SECRET_KEY = "not_so_secret_key"
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(app.root_path, 'database.db')