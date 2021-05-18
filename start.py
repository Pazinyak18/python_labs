from os.path import dirname, join, abspath
from flask_app.app import app
import flask_app.endpoints
import logging
from database import create_db

if __name__ == '__main__':
    create_db(app)
    logging.basicConfig(filename=join(dirname(dirname(abspath(__file__))), "flask_log.log"), level=logging.INFO)
    app.run(debug=True)
