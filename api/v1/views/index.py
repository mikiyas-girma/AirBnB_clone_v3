#!/usr/bin/python3
''' just used for routing to different parts of the api'''

from models import storage
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from flask import jsonify
from api.v1.views import app_views

classes = {
    "users": User,
    "places": Place,
    "states": State,
    "cities": City,
    "amenities": Amenity,
    "reviews": Review
}


@app_views.route('/status', methods=['GET'])
def status():
    ''' routes to status page '''
    return jsonify({"status": "OK"})
