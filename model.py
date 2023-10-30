from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.Text, nullable=False)
    password = db.Column(db.Text, nullable=False)
    email = db.Column(db.Text, nullable=False)
    is_admin = db.Column(db.Boolean, nullable=False, default=False)

    admin = db.relationship('admin', backref='users', lazy=True)

class admin(db.Model):
    __tablename__ = 'admin'
    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.Text, nullable=False)
    address = db.Column(db.Text, nullable=False)
    phone_number = db.Column(db.integer, nullable=False)
    profile_picture = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Boolean, nullable=False, default=True)

    user = db.relationship('User', backref='admin', lazy=True)
    adminAnalyticsData = db.relationship('adminAnalyticsData', backref='admin', lazy=True)

class adminAnalyticsData(db.Model):
    __tablename__ = 'adminAnalyticsData'
    id = db.Column(db.Integer, primary_key=True)
    admin_id = db.Column(db.Integer, nullable=False)
    total_users = db.Column(db.Integer, nullable=False)
    total_transactions = db.Column(db.Integer, nullable=False)
    total_amount = db.Column(db.Integer, nullable=False)
    total_commission = db.Column(db.Integer, nullable=False)
    transaction_approved = db.Column(db.Integer, nullable=False)
    transaction_disapproved = db.Column(db.Integer, nullable=False)
    admin_id = db.Column(db.Boolean, nullable=False, default=True)

    admin = db.relationship('admin', backref='adminAnalyticsData', lazy=True)