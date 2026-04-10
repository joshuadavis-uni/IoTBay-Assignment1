import re
from backend.models.user import User

def validate_email(email):
    """
    Checks if the email is in a valid format e.g. example@email.com
    re.match uses a regular expression pattern to validate the format
    """
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email) is not None

def validate_password(password):
    """
    Checks password meets requirements:
    - At least 6 characters long
    - At least one uppercase letter
    - At least one lowercase letter
    - At least one number
    - At least one special character (@, $, #, %)
    """
    if len(password) < 6 or len(password) > 20:
        return False, "Password must be between 6 and 20 characters"
    if not re.search(r'[A-Z]', password):
        return False, "Password must contain at least one uppercase letter"
    if not re.search(r'[a-z]', password):
        return False, "Password must contain at least one lowercase letter"
    if not re.search(r'[0-9]', password):
        return False, "Password must contain at least one number"
    if not re.search(r'[@$#%]', password):
        return False, "Password must contain at least one special character (@$#%)"
    return True, "Valid"

def register_user(full_name, email, password, phone='', address='', user_type='customer'):
    """
    Handles the registration logic:
    1. Validates the email format
    2. Validates the password format
    3. Creates the user in the database
    Returns a dict with success status and a message
    """
    
    if not full_name or not email or not password:
        return {'success': False, 'message': 'Name, email and password are required'}

    # Validate email format
    if not validate_email(email):
        return {'success': False, 'message': 'Invalid email format'}

    
    is_valid, message = validate_password(password)
    if not is_valid:
        return {'success': False, 'message': message}

    
    user_id = User.create(full_name, email, password, phone, address, user_type)
    if user_id is None:
        return {'success': False, 'message': 'Email already registered'}

    return {
        'success': True,
        'message': 'Registration successful',
        'user_id': user_id,
        'full_name': full_name,
        'email': email,
        'user_type': user_type
    }

def login_user(email, password):
    """
    Handles the login logic:
    1. Validates email format
    2. Looks up the user by email
    3. Checks the password matches
    Returns a dict with success status and user details if successful
    """
    
    if not validate_email(email):
        return {'success': False, 'message': 'Invalid email format'}

    
    user = User.get_by_email(email)
    if user is None:
        return {'success': False, 'message': 'Email not found'}

   
    if user.password != password:
        return {'success': False, 'message': 'Incorrect password'}

    
    if user.status != 'active':
        return {'success': False, 'message': 'Account is inactive'}

    return {
        'success': True,
        'message': 'Login successful',
        'user_id': user.user_id,
        'full_name': user.full_name,
        'email': user.email,
        'user_type': user.user_type
    }