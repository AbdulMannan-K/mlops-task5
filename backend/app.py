from flask import Flask, request, jsonify
from pymongo import MongoClient

# Initialize Flask app
application = Flask(__name__)

# Connect to MongoDB
mongo_client = MongoClient("mongodb://localhost:27017")
database = mongo_client["user_database"]
user_collection = database["user_data"]

@application.route('/submit', methods=['POST'])
def submit_user_data():
    user_data = request.json
    user_name = user_data.get('name')
    user_email = user_data.get('email')
    user_collection.insert_one({'name': user_name, 'email': user_email})
    return jsonify(message='User data saved successfully.')

if __name__ == '__main__':
    application.run(debug=True, host='0.0.0.0')
