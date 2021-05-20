from os.path import dirname, join, abspath
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from marshmallow import validate, fields, post_load
from marshmallow_enum import EnumField
from enum import Enum


db = SQLAlchemy()
ma = Marshmallow()


class Genre(Enum):
    Rock = 0
    Rap = 1
    Pop = 2


class Album(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), nullable=False)
    band = db.Column(db.String(32), nullable=False)
    type_of_genre = db.Column(db.Enum(Genre))
    amount_of_songs = db.Column(db.Integer, nullable=False)
    duration_in_sec = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=False)

    def __init__(self, name: str = " ", band: str = " ", type_of_genre: Genre = 0, amount_of_songs: int = 0,
                 duration_in_sec: int = 0, price: float = 0):
        self.name = name
        self.band = band
        self.type_of_genre = type_of_genre
        self.amount_of_songs = amount_of_songs
        self.duration_in_sec = duration_in_sec
        self.price = price

    def __str__(self):
        return f"Name: {self.name}\n " \
               f"Band:{self.band}\n " \
               f"genre: {self.type_of_genre}\n " \
               f"Amount of songs: {self.amount_of_songs}\n " \
               f"Duration: {self.duration_in_sec}\n " \
               f"Price: {self.price}\n"


class AlbumSchema(ma.Schema):
   
    name = fields.Str(validate=validate.Length(min=1, max=32))
    band = fields.Str(validate=validate.Length(min=1, max=32))
    type_of_genre = EnumField(Genre)
    amount_of_songs = fields.Int(validate=validate.Range(min=1, max=9999))
    duration_in_sec = fields.Int(validate=validate.Range(min=1, max=99999999))
    price = fields.Float(validate=validate.Range(min=0.0, max=9999.999))

 
    @post_load
    def make_album(self, data, **kwargs):
        return Album(**data)


album_schema = AlbumSchema()
albums_schema = AlbumSchema(many=True)


def create_db(app):
    try:
        db.create_all(app=app)
    except Exception as e:
        print(e)
        print("CANNOT CONNECT TO DB(CHECK config.py SQLALCHEMY_DATABASE_URI IF THIS FIELD IS OK) CREATING SQLITE DB")
        dbdir = join(dirname(dirname(abspath(__file__))), "database")
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + join(dbdir, 'db.sqlite')
        db.create_all(app=app)
