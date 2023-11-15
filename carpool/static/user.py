# app/user.py
from flask import Flask, render_template, request, redirect, url_for, jsonify

app = Flask(__name__)

class User:
    def __init__(self):
        self.username = None
        self.email = None
        self.password = None
        self.first_name = None
        self.last_name = None
        self.birthday = None
        self.from_location = None
        self.to_location = None
        self.datetime = None
        self.car = None
        self.passengers = None
        self.phone_number = None

    def login(self, email, password):
        # Placeholder implementation for login logic
        return email == self.email and password == self.password

    def signup_first_page(self, username, email, password, first_name, last_name, birthday):
        # Placeholder implementation for signup first page logic
        self.username = username
        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.birthday = birthday

    def signup_second_page(self, from_location, to_location, datetime, car, passengers, phone_number):
        # Placeholder implementation for signup second page logic
        self.from_location = from_location
        self.to_location = to_location
        self.datetime = datetime
        self.car = car
        self.passengers = passengers
        self.phone_number = phone_number

user = User()

@app.route('/')
def landing():
    return render_template('landing.html')

@app.route('/index', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        action = request.form.get('action')

        if action == 'login':
            return redirect(url_for('login'))
        elif action == 'signup':
            return redirect(url_for('signup_first_page'))
        else:
            return "Invalid action."

    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        if user.login(email, password):
            return "Login successful!"
        else:
            return "Login failed. Please check your email and password."

    return render_template('login.html')

@app.route('/signup/first_page', methods=['GET', 'POST'])
def signup_first_page():
    if request.method == 'POST':
        user.signup_first_page(
            username=request.form.get('username'),
            email=request.form.get('email'),
            password=request.form.get('password'),
            first_name=request.form.get('first_name'),
            last_name=request.form.get('last_name'),
            birthday=request.form.get('birthday')
        )
        return redirect(url_for('signup_second_page'))

    return render_template('signup_first_page.html')

@app.route('/signup/second_page', methods=['POST'])
def signup_second_page():
    if request.method == 'POST':
        user.signup_second_page(
            from_location=request.form.get('from_location'),
            to_location=request.form.get('to_location'),
            datetime=request.form.get('datetime'),
            car=request.form.get('car'),
            passengers=request.form.get('passengers'),
            phone_number=request.form.get('phone_number')
        )

        # You can store the complete user data in the session or database.
        # Redirect or return a response as needed.
        return "Signup completed. Welcome to our service!"

    return render_template('signup_second_page.html')

if __name__ == '__main__':
    app.run(debug=True)
