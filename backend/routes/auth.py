from flask import Blueprint, request, jsonify, session
from backend.controllers.auth_controller import register_user, login_user

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/auth/register', methods=['POST'])
def register():
    """
    Handles POST requests to /auth/register
    Expects JSON data with: full_name, email, password, phone (optional), address (optional)
    """

    data = request.get_json()


    full_name = data.get('full_name')
    email = data.get('email')
    password = data.get('password')
    phone = data.get('phone', '')       
    address = data.get('address', '')   
    user_type = data.get('user_type', 'customer')  

   
    result = register_user(full_name, email, password, phone, address, user_type)

    if result['success']:
       
        session['user_id'] = result['user_id']
        session['full_name'] = result['full_name']
        session['email'] = result['email']
        session['user_type'] = result['user_type']
        return jsonify(result), 201  
    else:
        return jsonify(result), 400  

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

        session['user_id'] = result['user_id']
        session['full_name'] = result['full_name']
        session['email'] = result['email']
        session['user_type'] = result['user_type']
        return jsonify(result), 200  
    else:
        return jsonify(result), 401 

@auth_bp.route('/auth/logout', methods=['POST'])
def logout():
    """
    Handles POST requests to /auth/logout
    Clears the server side session
    """
    session.clear()  
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