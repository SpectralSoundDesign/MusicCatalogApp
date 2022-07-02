from code import interact
from email.policy import default
from enum import unique
from pytz import timezone

from sqlalchemy import Integer
from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class MusicCatalog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    composerName = db.Column(db.String(50))
    pieceName = db.Column(db.String(100))
    pieceDate = db.Column(db.String(10))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    note_data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    musicCatalog = db.relationship('MusicCatalog')

