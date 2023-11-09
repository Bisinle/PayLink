import pytest
from api import User, User_Profile, Beneficiary, UserBeneficiary, Transaction, WalletActivity, Category, Wallet

# Test User schema
def test_user_schema():
    user = User(user_name="test_user", password_hash="password")
    serialized_user = User_Schema().dump(user)

    assert serialized_user["user_name"] == user.user_name
    assert serialized_user["password_hash"] is not None

# Test User_Profile schema
def test_user_profile_schema():
    user_profile = User_Profile(first_name="Test", last_name="User")
    serialized_user_profile = UserProfile_Schema().dump(user_profile)

    assert serialized_user_profile["first_name"] == user_profile.first_name
    assert serialized_user_profile["last_name"] == user_profile.last_name

# Test Beneficiary schema
def test_beneficiary_schema():
    beneficiary = Beneficiary(name="Test Beneficiary")
    serialized_beneficiary = Beneficiary_Schema().dump(beneficiary)

    assert serialized_beneficiary["name"] == beneficiary.name

# Test Transaction schema
def test_transaction_schema():
    transaction = Transaction(amount=100, sender_id=1, receiver_account="1234567890")
    serialized_transaction = transaction_Schema().dump(transaction)

    assert serialized_transaction["amount"] == 100
    assert serialized_transaction["sender_id"] == 1
    assert serialized_transaction["receiver_account"] == "1234567890"

# Test WalletActivity schema
def test_wallet_activity_schema():
    wallet_activity = WalletActivity(transaction_id=1, amount=100, transaction_type="sent")
    serialized_wallet_activity = wallet_activity_Schema().dump(wallet_activity)

    assert serialized_wallet_activity["transaction_id"] == 1
    assert serialized_wallet_activity["amount"] == 100
    assert serialized_wallet_activity["transaction_type"] == "sent"

# Test Category schema
def test_category_schema():
    category = Category(type="expense")
    serialized_category = category_Schema().dump(category)

    assert serialized_category["type"] == "expense"

# Test Wallet schema
def test_wallet_schema():
    wallet = Wallet(user_prof_id=1, balance=100, type="savings")
    serialized_wallet = wallet_Schema().dump(wallet)

    assert serialized_wallet["user_prof_id"] == 1
    assert serialized_wallet["balance"] == 100
    assert serialized_wallet["type"] == "savings"