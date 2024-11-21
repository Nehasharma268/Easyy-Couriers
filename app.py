from flask import Flask, render_template, request, redirect, url_for # type: ignore
import mysql.connector # type: ignore
import bcrypt # Make sure to install bcrypt with `pip install bcrypt`

app = Flask(__name__)

# Configure database connection
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Shyambaran26#",
        database="CourierManagement"
    )

# Home page route
@app.route('/')
def index():
    return render_template('index.html')

# Booking form route
@app.route('/booking', methods=['GET', 'POST'])
def booking():
    if request.method == 'POST':
        # Retrieve form data
        sender_name = request.form['sender_name']
        sender_address = request.form['sender_address']
        receiver_name = request.form['receiver_name']
        receiver_address = request.form['receiver_address']
        weight = request.form['parcel_weight']

        # Save form data to the database (insert query)
        db = get_db_connection()
        cursor = db.cursor()
        query = "INSERT INTO Parcels (sender_name, sender_address, receiver_name, receiver_address, weight) VALUES (%s, %s, %s, %s, %s)"
        values = (sender_name, sender_address, receiver_name, receiver_address, weight)
        cursor.execute(query, values)
        db.commit()
        cursor.close()
        db.close()

        return redirect(url_for('index'))

    return render_template('booking.html')

# Status update form route
@app.route('/status_update', methods=['GET', 'POST'])
def status_update():
    if request.method == 'POST':
        # Retrieve form data
        parcel_id = request.form['parcel_id']
        status = request.form['status']

        # Update status in the database (insert query)
        db = get_db_connection()
        cursor = db.cursor()
        query = "INSERT INTO DeliveryStatus (parcel_id, status) VALUES (%s, %s)"
        values = (parcel_id, status)
        cursor.execute(query, values)
        db.commit()
        cursor.close()
        db.close()

        return redirect(url_for('index'))

    return render_template('status_update.html')


# Feedback form route
@app.route('/feedback', methods=['GET', 'POST'])
def feedback():
    if request.method == 'POST':
        # Retrieve form data
        name = request.form['name']
        email = request.form['email']
        message = request.form['feedback']

        # Save feedback to the database (insert query)
        db = get_db_connection()
        cursor = db.cursor()
        query = "INSERT INTO Feedback (name, email, message) VALUES (%s, %s, %s)"
        values = (name, email, message)
        cursor.execute(query, values)
        db.commit()
        cursor.close()
        db.close()

        return redirect(url_for('index'))

    return render_template('feedback.html')

# Login route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db_connection()
        cursor = db.cursor(dictionary=True)
        cursor.execute("SELECT * FROM Users WHERE username = %s AND password = %s", (username, password))
        user = cursor.fetchone()
        cursor.close()
        db.close()

        if user:
            return redirect(url_for('dashboard', username=username))
        else:
            return render_template('login.html', error=True)
    return render_template('login.html')  # Render login form for GET requests


# Dashboard route
@app.route('/dashboard')
def dashboard():
    username = request.args.get('username', 'User')
    return render_template('dashboard.html', username=username)

if __name__ == '__main__':
    app.run(debug=True)
