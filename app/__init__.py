from flask import Flask

from .db import init_db
from .routes import routes

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:postgres@localhost:5432/postgres"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.register_blueprint(routes)

init_db(app)
