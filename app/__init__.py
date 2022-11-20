from flask import Flask

from .db import init_db
from .routes import routes

from config import DATABASE_URL

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.register_blueprint(routes)

init_db(app)
