from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS #Cross origin requests

app = Flask(__name__)

CORS(app) #It's okay for the backend to talk to the frontend (since they are different servers)

#config allows us to enable/disable certain settings such as debug mode and CORS
#SQLAlchemy is used to make it easier to interact with the database
#_DATABASE_URI is the location of the database (URI is unique identifier), but this could've easily been a file

app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///mydatabase.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#False is recommended for performance, because we dont want to track every CRUD operation on the database

db = SQLAlchemy(app) #create an instance of the database