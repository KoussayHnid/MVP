from flask import Flask, render_template, request
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://localhost:27017/carpool.drivers'
mongo = PyMongo(app)
db = mongo.db 
drivers_collection = db.drivers
@app.route('/')
def index():
    return render_template('find.html')

@app.route('/search', methods=['GET', 'POST'])
def search_rides():
    from_location = request.form.get('from_location')
    to_location = request.form.get('to_location')
    datetime = request.form.get('datetime')

    print(f"From: {from_location}, To: {to_location}, Datetime: {datetime}")
    print(f"Mongo URI: {app.config['MONGO_URI']}")

    drivers = drivers_collection.find({
        'from_location': from_location,
        'to_location': to_location,
        'datetime': datetime
    })

    count_of_documents = drivers_collection.count_documents({
        'from_location': from_location,
        'to_location': to_location,
        'datetime': datetime
    })
    print(f"Number of documents retrieved: {count_of_documents}")

    return render_template('find2.html', drivers=drivers)

if __name__ == '__main__':
    app.run(debug=True)
