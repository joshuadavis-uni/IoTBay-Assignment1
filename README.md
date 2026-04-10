# IoTBay-Assignment1# IoTBay - Assignment 1

A web-based IoT device marketplace built with Flask (backend) and HTML/CSS/JavaScript (frontend), using SQLite as the database.

## Group Information

**Subject:** 41025 Introduction to Software Development  
**Workshop:** Workshop 2  
**Group:** 4  

## Branch
All submission code is on the `main` branch.

## Dependencies
All dependencies are listed in `requirements.txt`.

### Backend (Python)
- Python 3.x
- Flask 3.1.3
- Flask-CORS 6.0.2

### Frontend
- No additional dependencies — pure HTML, CSS and JavaScript.




## How to Run

### 1. Clone the repository
```bash
git clone https://github.com/joshuadavis-uni/IoTBay-Assignment1
cd IoTBay-Assignment1
```

### 2. Create and activate a virtual environment
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Initialise the database
```bash
python -m backend.models.db_init
```
This creates the `iotbay.db` SQLite database file with all required tables.

### 5. Start the backend server
Open a terminal and run:
```bash
python -m backend.app
```
The Flask backend will run at: `http://127.0.0.1:8080`

### 6. Start the frontend server
Open a **second terminal** and run:
```bash
python -m http.server 8000 --directory ./frontend/
```
The frontend will run at: `http://127.0.0.1:8000`

### 7. Open in browser
Go to: `http://127.0.0.1:8000`

## R0 Features Implemented
- **Home** — landing page with links to Login and Register
- **Register** — create an account with email and password validation
- **Login** — login with credentials validated against the database
- **Welcome** — displays the logged in user's name and email
- **Logout** — clears session and redirects to home

## Test Credentials
Register a new account with the following password requirements:
- 6 to 20 characters
- At least one uppercase letter
- At least one lowercase letter  
- At least one number
- At least one special character (@, $, #, %)

**Example:** `Password@1`