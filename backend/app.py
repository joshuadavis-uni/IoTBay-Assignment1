from flask import Flask
from flask_cors import CORS
from backend.models.db_init import init_db

app = Flask(__name__)
CORS(app, supports_credentials=True)

init_db()

@app.route('/')
def home():
    return 'IoTBay backend is running!'

if __name__ == '__main__':
    app.run(debug=True, port=8080)