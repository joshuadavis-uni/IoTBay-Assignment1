from flask import Flask
from flask_cors import CORS
from backend.models.db_init import init_db
from backend.routes.auth import auth_bp

app = Flask(__name__)

# Secret key is required for Flask sessions to work
# In a real app this would be a long random string stored in an environment variable
app.secret_key = 'iotbay-secret-key-2026'

CORS(app, supports_credentials=True, origins=["http://127.0.0.1:8000"])

# Register the auth blueprint so Flask knows about our routes
app.register_blueprint(auth_bp)

# Initialise the database when the app starts
init_db()

@app.route('/')
def home():
    return 'IoTBay backend is running!'

if __name__ == '__main__':
    app.run(debug=True, port=8080)