from flask import Flask, render_template, request, redirect, url_for
from flask_pymongo import PyMongo
from datetime import datetime

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/my_db"
mongo = PyMongo(app)
# client = MongoClient('mongodb://localhost:27017/')
# db = client['my_db']
# riders_collection = db['riders']
# search_riders_collection = db['search_riders']

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/signin', methods=['GET', 'POST'])
def signin():
    try:
        firstname = request.form.get('firstname')
        lastname = request.form.get('lastname')
        email = request.form.get('email')
        password = request.form.get('password')
        birthday = request.form.get('birthday')
        gender = request.form.get('gender')
        print(firstname)
        mongo.db.riders.insert_one({
            'firstname': firstname,
            'lastname': lastname,
            'email': email,
            'password': password,
            'birthday': birthday,
            'gender': gender
        })
        return redirect(url_for('post2.html'))
    except:
        return render_template('post1.html')

@app.route('/post2', methods=['GET', 'POST'])
def post2():
    if request.method == 'POST':
        from_location = request.form['from_location']
        to_location = request.form['to_location']
        datetime_str = request.form['datetime']
        datetime_obj = datetime.strptime(datetime_str, '%Y-%m-%dT%H:%M')
        car_brand = request.form['car_brand']
        num_seats = int(request.form['num_seats'])
        price = float(request.form['price'])
        phone_number = request.form['phone_number']

        riders_collection.update_one(
            {'$set': {
                'from_location': from_location,
                'to_location': to_location,
                'datetime': datetime_obj,
                'car_brand': car_brand,
                'num_seats': num_seats,
                'price': price,
                'phone_number': phone_number
            }}
        )
        return redirect(url_for('home'))
    return render_template('post2.html')

@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        from_location = request.form['from_location']
        to_location = request.form['to_location']
        datetime_str = request.form['datetime']
        num_persons = int(request.form['num_persons'])

        search_riders_collection.insert_one({
            'from_location': from_location,
            'to_location': to_location,
            'datetime': datetime.strptime(datetime_str, '%Y-%m-%dT%H:%M'),
            'num_persons': num_persons
        })

        return redirect(url_for('home'))

    return render_template('find.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
