from flask import Flask, request, jsonify, make_response
from flask_migrate import Migrate
from model import db, User, admin, adminAnalyticsData

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///paylink.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)

@app.route('/user/<int:user_id>', methods=['GET'])
def get_user_by_id(user_id):
    user = User.query.get(user_id)
    if user:
        user_data = {
            'id': user.id,
            'username': user.username,
            'email': user.email,
            'is_admin': user.is_admin
            # Add more fields as needed
        }
        return jsonify(user_data)
    return jsonify({'error': 'User not found'}), 404

# Route to update user information by ID
@app.route('/user/<int:user_id>', methods=['PUT'])
def update_user_by_id(user_id):
    user = User.query.get(user_id)
    if user:
        data = request.get_json()
        user.username = data.get('username', user.username)
        user.email = data.get('email', user.email)
        user.is_admin = data.get('is_admin', user.is_admin)
        # Update other fields as needed
        db.session.commit()
        return jsonify({'message': 'User updated successfully'})
    return jsonify({'error': 'User not found'}), 404

# Route to get adminAnalyticsData
@app.route('/adminanalytics', methods=['GET'])
def get_admin_analytics():
    admin_analytics = adminAnalyticsData.query.all()
    analytics_data = []
    for analytics in admin_analytics:
        data = {
            'id': analytics.id,
            'total_users': analytics.total_users,
            'total_transactions': analytics.total_transactions,
            'total_amount': analytics.total_amount,
            'total_commission': analytics.total_commission,
            'transaction_approved': analytics.transaction_approved,
            'transaction_disapproved': analytics.transaction_disapproved,
            'admin_id': analytics.admin_id
            # Add more fields as needed
        }
        analytics_data.append(data)
    return jsonify(analytics_data)

if __name__ == '__main__':
    app.run(debug=True)