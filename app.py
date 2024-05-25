from flask import Flask
from pymongo import MongoClient
from config import Config
from routes.lecturer_routes import lecturer_bp
from flask_cors import CORS

app = Flask(__name__)
app.config.from_object(Config)

CORS(app)

mongo_client = MongoClient(app.config['MONGO_URI'])
app.config['DB'] = mongo_client.lecturer_service

app.register_blueprint(lecturer_bp, url_prefix=None)

if __name__ == '__main__':
    app.run(host='0.0.0.0' ,debug=True)