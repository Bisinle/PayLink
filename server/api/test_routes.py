import pytest
from api import User, User_Profile, Beneficiary, UserBeneficiary, Transaction, WalletActivity, Category, Wallet

# Test signup
def test_signup():
    data = {
        "user_name": "test_user",
        "password": "password",
        "first_name": "Test",
        "last_name": "User",
        "address": "123 Main Street",
        "phone_number": "1234567890",
        "email": "test@example.com",
    }

    response = auth.post("/signup", json=data)
    assert response.status_code == 200

# Test login
def test_login():
    data = {
        "username": "test_user",
        "password": "password",
    }

    response = auth.post("/login", json=data)
    assert response.status_code == 200

    access_token = response.json["access_token"]

# Test get all users
def test_get_all_users():
    response = ns.get("/users")
    assert response.status_code == 200

# Test create wallet
def test_create_wallet():
    data = {
        "user_prof_id": 1,
        "type": "savings",
    }

    response = wallet.post("/wallet", json=data)
    assert response.status_code == 200

# Test update wallet balance
def test_update_wallet_balance():
    data = {
        "amount": 100,
    }

    response = wallet.post("/wallet/1", json=data)
    assert response.status_code == 200

# Test get all transactions
def test_get_all_transactions():
    response = transactions.get("/transactions")
    assert response.status_code == 200

# Test create transaction
def test_create_transaction():
    data = {
        "amount": 100,
        "receiver_account": "1234567890",
        "sender_id": 1,
        "category": "expense",
    }

    response = transactions.post("/transactions", json=data)
    assert response.status_code == 200

# Test get all wallet activities
def test_get_all_wallet_activities():
    response = wallet.get("/wallet-Activity")
    assert response.status_code == 200