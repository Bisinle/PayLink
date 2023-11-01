from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData,UniqueConstraint
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.orm import validates
from sqlalchemy.ext.hybrid import hybrid_property
from werkzeug.security import generate_password_hash,check_password_hash




metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)




class User(db.Model):
    __tablename__ ='users'

    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String)
    public_id = db.Column(db.String(50))
    _password = db.Column(db.String)
    is_admin =  db.Column(db.Integer)
    # email = db.Column(db.String)
    joined = db.Column(db.DateTime, server_default=db.func.now())




  

    __table_args__ = (UniqueConstraint("public_id","user_name", name="User_unique_constraint"),)

    @hybrid_property
    def password_hash(self):
        return self._password
    
    @password_hash.setter
    def password_hash(self, password):
        self._password = generate_password_hash(password,method='pbkdf2:sha256')

    def authenticate(self,password):
        return True if check_password_hash(self._password, password) else False



    def __repr__(self):
        return f'(id: {self.id}, user_name: {self.user_name}, is_admin: {self.is_admin},  joined: {self.joined} )'






class User_Profile(db.Model):
    __tablename__ ='users_profile'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    address=db.Column(db.String)
    phone_number=db.Column(db.Integer)
    Account=db.Column(db.Integer)
    profile_pictur= db.Column(db.String)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user = db.relationship('User', backref='users_profile',uselist=False)

    wallet = db.relationship('Wallet', back_populates='user_profile', cascade='all,delete-orphan',uselist=False)
    transactions = db.relationship('Transaction', backref='user_profile', lazy=True)
    wallet_ctivities = db.relationship('WalletActivity', backref='user_profile', lazy=True)

    

    # beneficiary relationship
    user_beneficiary_association = db.relationship('UserBeneficiary', back_populates='user',cascade='all, delete-orphan')
    beneficiaries = association_proxy('user_beneficiary_association','beneficiary')


 

    def __repr__(self):
        return f'(id: {self.id}, first_name: {self.first_name},last_name: {self.last_name}, address: {self.address},  phone: {self.phone_number} )'





class UserBeneficiary(db.Model):
    __tablename__='user_beneficiaries'  
    
    
    id = db.Column(db.Integer, primary_key=True)    
    sender_id = db.Column('sender_id',db.Integer, db.ForeignKey("users_profile.id"))
    beneficiary_id = db.Column('beneficiary_id',db.Integer, db.ForeignKey("beneficiaries.id"))

    user = db.relationship('User_Profile', back_populates='user_beneficiary_association')
    beneficiary = db.relationship('Beneficiary', back_populates='user_beneficiary_association')

    def save(self):
        db.session.add(self)
        db.session.commit()

    # def __repr__(self):
    #     return f'(id: {self.id}, sender_id: {self.sender_id},beneficiary_id: {self.beneficiary_id} )'






class Beneficiary(db.Model):
    __tablename__ ='beneficiaries'
    pass

    id = db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String)
    Account=db.Column(db.String)




    # # beneficiary relationship
    user_beneficiary_association = db.relationship('UserBeneficiary', back_populates='beneficiary')
    users = association_proxy('user_beneficiary_association','user')

    def save(self):
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return f'(id: {self.id}, benef_name: {self.name}, benef_Account: {self.Account}  )'





class Transaction(db.Model):
    __tablename__ ='transactions'

    id = db.Column(db.Integer, primary_key=True)
    amount=db.Column(db.Integer)
    receiver_account=db.Column(db.Integer)
    created = db.Column(db.DateTime, server_default=db.func.now())

    sender_id = db.Column(db.Integer, db.ForeignKey('users_profile.id'), nullable=False)

    wallet_ctivities = db.relationship('WalletActivity', backref='transaction', lazy=True)

    
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'))
    category = db.relationship('Category', backref='transaction',uselist=False)


    def save(self):
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return f'(id: {self.id}, amount: {self.amount},sender_id: {self.sender_id} ,receiver_account: {self.receiver_account}, status: {self.status} )'



class WalletActivity(db.Model):
    __tablename__ ='wallet_activities'
    
    id = db.Column(db.Integer, primary_key=True)
    transaction_type = db.Column(db.String(50))  # E.g., 'sent', 'received', 'top-up'
    amount = db.Column(db.Float)
    description = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, server_default=db.func.now())

    user_id = db.Column(db.Integer, db.ForeignKey('users_profile.id'), nullable=False)
    transaction_id = db.Column(db.Integer, db.ForeignKey('transactions.id'), nullable=False)






class Category(db.Model):
    __tablename__ ='categories'

    id = db.Column(db.Integer, primary_key=True)
    type=db.Column(db.String)



class Wallet(db.Model):
    __tablename__ ='wallets'

    id = db.Column(db.Integer, primary_key=True)   
    balance =  db.Column(db.Integer)
    type=db.Column(db.String)
    status=db.Column(db.String)
    Account=db.Column(db.String)
    

    joined = db.Column(db.DateTime, server_default=db.func.now())


    user_prof_id = db.Column(db.Integer, db.ForeignKey('users_profile.id'))
    user_profile = db.relationship('User_Profile', back_populates='wallet', )

 

    
    def transaction_fees(self,amount):
        deductionA= 0
        deductionB= 0.01
        deductionC= 0.024
        deductionD= 0.0028
        deductionE= 0.003
        deductionF =0.004
        amount =float(amount)
        deduction =0
        if 0<=amount<=5000:
            deduction = amount * deductionA
        if 5001<=amount<=15000:
            deduction = amount * deductionB
        if 1501<=amount<=30000:
            deduction = amount * deductionC
        if 30001<=amount<=55000:
            deduction = amount * deductionD
        if 55001<=amount<=100000:
            deduction = amount * deductionE
    
        if 50000<=amount<=100000:
            deduction = amount * deductionB
        else:
            deduction = amount * deductionF
            
        
        
    
        return deduction


    def save(self):
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return f'(id: {self.id}, balance: {self.balance},user_id: {self.user_prof_id}  )'







# UserProfile:
# Fields:
# Profile ID (auto-generated)
# User (foreign key to User)
# Full Name
# Address
# Phone Number
# Profile Picture (image upload)


# Beneficiary:
# Fields:
# Beneficiary ID (auto-generated)
# User (foreign key to User)
# Beneficiary User (foreign key to User for the contact)



# Transaction:
# Fields:
# Transaction ID (auto-generated)
# Sender (foreign key to User)
# Receiver (foreign key to User)
# Amount
# Date and Time
# Status (e.g., completed, pending)


# Admin:
# Fields:
# Admin ID (auto-generated)
# Username
# Password (hashed and salted)




# TransactionLog (for Admin):
# Fields:
# Log ID (auto-generated)
# Admin (foreign key to Admin)
# User (foreign key to User, nullable)
# Transaction (foreign key to Transaction)
# Action (e.g., create, read, update, delete)
# Date and Time



# AnalyticsData:
# Fields:
# Analytics ID (auto-generated)
# User (foreign key to User, nullable)
# Transaction (foreign key to Transaction, nullable)
# Profit (if applicable)
# Date and Time