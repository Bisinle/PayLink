import pytest
from sqlalchemy import create_engine

'''from your_code import User, User_Profile, Beneficiary, UserBeneficiary, Transaction, WalletActivity, Category, Wallet'''

engine = create_engine("sqlite:///tests.db")

@pytest.fixture
def session():
    session = User.session_factory()
    yield session
    session.close()

def test_user_can_create_new_user_profile(session):
    user = User(user_name="test_user", password_hash="password")
    user_profile = User_Profile(user=user, first_name="Test", last_name="User")

    session.add(user_profile)
    session.commit()

    assert session.query(User_Profile).get(user_profile.id) is not None

def test_user_profile_can_have_many_beneficiaries(session):
    user = User(user_name="test_user", password_hash="password")
    user_profile = User_Profile(user=user, first_name="Test", last_name="User")
    beneficiary1 = Beneficiary(user_profile=user_profile)
    beneficiary2 = Beneficiary(user_profile=user_profile)

    session.add_all([user, user_profile, beneficiary1, beneficiary2])
    session.commit()

    assert len(session.query(Beneficiary).filter(Beneficiary.user_profile_id == user_profile.id).all()) == 2

def test_user_can_create_new_transaction(session):
    user = User(user_name="test_user", password_hash="password")
    user_profile = User_Profile(user=user, first_name="Test", last_name="User")
    transaction = Transaction(sender_id=user_profile.id, amount=100)

    session.add_all([user, user_profile, transaction])
    session.commit()

    assert session.query(Transaction).get(transaction.id) is not None

def test_transaction_can_have_wallet_activities(session):
    user = User(user_name="test_user", password_hash="password")
    user_profile = User_Profile(user=user, first_name="Test", last_name="User")
    transaction = Transaction(sender_id=user_profile.id, amount=100)
    wallet_activity = WalletActivity(transaction=transaction, amount=100, transaction_type="sent")

    session.add_all([user, user_profile, transaction, wallet_activity])
    session.commit()

    assert len(session.query(WalletActivity).filter(WalletActivity.transaction_id == transaction.id).all()) == 1