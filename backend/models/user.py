from backend.models.db_connect import get_db_connection

class User:
    def __init__(self, user_id, full_name, email, password, phone, address, user_type, status):
        self.user_id = user_id
        self.full_name = full_name
        self.email = email
        self.password = password
        self.phone = phone
        self.address = address
        self.user_type = user_type  
        self.status = status        

    @staticmethod
    def create(full_name, email, password, phone='', address='', user_type='customer'):
        """
        Inserts a new user into the database.
        Returns the new user's ID if successful, None if the email already exists.
        """
        conn = get_db_connection()
        cursor = conn.cursor()
        try:
            cursor.execute('''
                INSERT INTO users (full_name, email, password, phone, address, user_type)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (full_name, email, password, phone, address, user_type))
            conn.commit()
            return cursor.lastrowid  
        except Exception as e:
            print(f"Error creating user: {e}")
            return None  
        finally:
            conn.close()  

    @staticmethod
    def get_by_email(email):
        """
        Looks up a user by their email address.
        Returns a User object if found, None if not found.
        """
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM users WHERE email = ?', (email,))
        row = cursor.fetchone()
        conn.close()
        if row:
            return User(
                user_id=row['user_id'],
                full_name=row['full_name'],
                email=row['email'],
                password=row['password'],
                phone=row['phone'],
                address=row['address'],
                user_type=row['user_type'],
                status=row['status']
            )
        return None

    @staticmethod
    def get_by_id(user_id):
        """
        Looks up a user by their ID.
        Returns a User object if found, None if not found.
        """
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM users WHERE user_id = ?', (user_id,))
        row = cursor.fetchone()
        conn.close()
        if row:
            return User(
                user_id=row['user_id'],
                full_name=row['full_name'],
                email=row['email'],
                password=row['password'],
                phone=row['phone'],
                address=row['address'],
                user_type=row['user_type'],
                status=row['status']
            )
        return None