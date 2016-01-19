from datetime import datetime
from flask.ext.sqlalchemy import SQLAlchemy

class RiyadhSchools(db.Model):
    __tablename__ = 'riyadhSchools'
    id = db.Column(db.Integer, primary_key=True)
    school_name = db.Column(db.String(64))
    location = db.Column(db.String(64))
    phone = db.Column(db.Integer)
    discreption = db.Column(db.Text())
    rawdha = db.Column(db.Integer)
    tamhedy = db.Column(db.Integer)
    elementary = db.Column(db.Integer)
    intermediate = db.Column(db.Integer)
    highSchool = db.Column(db.Integer)
    gender = db.Column(db.String(64))
    lat = db.Column(db.Text())
    lng = db.Column(db.Text())

class RiyadhImages(db.Model):
    __tablename__ = 'riyadhImages'
    img = db.Column(db.Text())
    id = db.relationship('RiyadhSchools', foreign_keys=[RiyadhSchools.id])
