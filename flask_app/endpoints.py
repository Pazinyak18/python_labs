from flask import request, jsonify, abort
from marshmallow import ValidationError
from database import Album, album_schema, albums_schema, db
from .app import app


# endpoint to create new album
@app.route("/album", methods=["POST"])
def add_album():
    try:
        album = album_schema.load(request.json)
        db.session.add(album)
    except ValidationError as err:
        abort(400, err)
    db.session.commit()

    return jsonify(request.json)


# endpoint to show all albums
@app.route("/album", methods=["GET"])
def get_albums():
    all_albums = Album.query.all()
    result = albums_schema.dump(all_albums)
    return jsonify(result)


# endpoint to get album detail by id
@app.route("/album/<id>", methods=["GET"])
def album_detail(id):
    album = Album.query.get(id)
    if album is None:
        response = jsonify({
            'status': 404,
            'description': "id not found"
        })
        abort(404, response)

    return album_schema.jsonify(album)


# endpoint to update album
@app.route("/album/<id>", methods=["PUT"])
def album_update(id):
    album = Album.query.get(id)
    if not album:
        response = jsonify({
            'status': 404,
            'description': "id not found"
        })
        abort(404, response)
    try:
        album_req = album_schema.load(request.json)
        album.name = album_req.name
        album.band = album_req.band
        album.type_of_genre = album_req.type_of_genre
        album.amount_of_songs = album_req.amount_of_songs
        album.duration_in_sec = album_req.duration_in_sec
        album.price = album_req.price
    except ValidationError as err:
        abort(400, err)
    db.session.commit()
    return album_schema.jsonify(album)


# endpoint to delete technique
@app.route("/album/<id>", methods=["DELETE"])
def album_delete(id):
    album = Album.query.get(id)
    if album is None:
        response = jsonify({
            'status': 404,
            'description': "id not found"
        })
        abort(404, response)
    db.session.delete(album)
    db.session.commit()
    return album_schema.jsonify(album)
