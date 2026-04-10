from flask import Blueprint, request, jsonify, session
from backend.controllers.auth_controller import register_user, login_user

# A Blueprint is like a mini Flask app that handles a group of related routes
# Here we're grouping all authentication routes (login, register) together
auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/auth/register', methods=['POST'])
def register():
    """
    Handles POST requests to /auth/register
    Expects JSON data with: full_name, email, password, phone (optional), address (optional)
    """
    # Get the JSON data sent from the frontend
    data = request.get_json()

    # Extract each field from the data, .get() returns None if field doesn't exist
    full_name = data.get('full_name')
    email = data.get('email')
    password = data.get('password')
    phone = data.get('phone', '')       # optional, defaults to empty string
    address = data.get('address', '')   # optional, defaults to empty string
    user_type = data.get('user_type', 'customer')  # defaults to customer

    # Pass to the controller to handle the logic
    result = register_user(full_name, email, password, phone, address, user_type)

    if result['success']:
        # Store user info in session so we know who's logged in
        session['user_id'] = result['user_id']
        session['full_name'] = result['full_name']
        session['email'] = result['email']
        session['user_type'] = result['user_type']
        return jsonify(result), 201  # 201 means "Created" in HTTP
    else:
        return jsonify(result), 400  # 400 means "Bad Request" in HTTP

@auth_bp.route('/auth/login', methods=['POST'])
def login():
    """
    Handles POST requests to /auth/login
    Expects JSON data with: email, password
    """
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    result = login_user(email, password)

    if result['success']:
        # Store user info in session
        session['user_id'] = result['user_id']
        session['full_name'] = result['full_name']
        session['email'] = result['email']
        session['user_type'] = result['user_type']
        return jsonify(result), 200  # 200 means "OK" in HTTP
    else:
        return jsonify(result), 401  # 401 means "Unauthorised" in HTTP

@auth_bp.route('/auth/logout', methods=['POST'])
def logout():
    """
    Handles POST requests to /auth/logout
    Clears the server side session
    """
    session.clear()  # removes all data from the server session
    return jsonify({'success': True, 'message': 'Logged out successfully'}), 200

@auth_bp.route('/auth/session', methods=['GET'])
def get_session():
    """
    Handles GET requests to /auth/session
    Returns the current logged in user's details from the session
    The frontend calls this to check who is logged in
    """
    if 'user_id' in session:
        return jsonify({
            'logged_in': True,
            'user_id': session['user_id'],
            'full_name': session['full_name'],
            'email': session['email'],
            'user_type': session['user_type']
        }), 200
    else:
        return jsonify({'logged_in': False}), 200