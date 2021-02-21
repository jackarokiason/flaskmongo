from flask import Flask
from flask_pymongo import PyMongo
from decouple import config

app = Flask(__name__)

app.config['MONGO_URI'] = config('MONGO_URI')

mongo = PyMongo(app)
collection = mongo.db.student_name

@app.route('/')
def flask_mongodb_atlas():
    return "flask mongodb atlas!"

@app.route("/test")
def test():
    collection.insert({"Name": "Smith",
                         "Bid": "18cr",
                         "review": "good bowler"
})
    return "Connected to the data base!"

if __name__ == '__main__':
    app.run(port=8003, debug=True)