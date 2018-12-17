from datetime import datetime
from flask import flask, render_template 
from flask_sqlalchemy import SQLAlchemy
from pymongo import MongoClient

app = Flask(__name__)


app.config.update(dict(
    SQLALCHEMY_DATABASE_URI='mysql://root@localhost/shiyanlou',
    SQLALCHEMY_TRACK_MODIFICATIONS=False
))

db = SQLAlchemy(app)
mongo = MongoClient('127.0.0.1',27017).shiyanlou

class File(db.Model):
    __tablename__ = 'files'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=True)
    created_time = db.Column(db.DateTime)
    category_id = db.Column(db.Integer,db.ForeignKey('categories.id'))
    category = db.relationship('Category',uselist= False)
    content =db.Column(db.Text)


