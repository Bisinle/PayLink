import os
from flask import Flask,session
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask import request ,make_response,jsonify
from flask_cors import CORS
from flask_bcrypt import Bcrypt



from flask_marshmallow import Marshmallow

from flask_session import Session
from api.config import ApplicationConfig



# from flask_restx import Api, Resource, fields

# create both app and api instances
app = Flask(__name__)

CORS(app)

# CORS(app, supports_credentials=True)
# CORS(app, origins= "http://localhost:5173")
# CORS(app, methods=["GET", "POST", "PUT", "DELETE"])
# CORS(app, allow_headers=["Content-Type"])
bcrypt = Bcrypt(app)

ma = Marshmallow(app)


app.config['SECRET_KEY'] ='mysecret'
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite3"
app.config['SESSION_TYPE'] = 'sqlalchemy'

from api.models import db,User,User_Profile,Wallet,Transaction,Beneficiary,Category,WalletActivity,UserBeneficiary


migrate = Migrate(app, db)
db.init_app(app)
app.config['SESSION_SQLALCHEMY']=db
Session(app)
# with app.app_context():
#     db.create_all()

# from  api import routes
# with app.app_context():
#   db.create_all()