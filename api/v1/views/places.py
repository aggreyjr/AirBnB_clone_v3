#!/usr/bin/python3
'''Places API View'''

from flask import abort, jsonify, make_response, request
import requests
from api.v1.views import app_views
from api.v1.views.amenities import amenities
from api.v1.views.places_amenities import place_amenities
from models import storage
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.state import State
from models.user import User
import json
from os import getenv


@app_views.route('cities/<city_id>/places',
                 methods=['GET'], strict_slashes=False)
def place(city_id):
    """
    Retrieves the list of all Place objects of a City.

    Args:
        city_id (str): The ID of the City.

    Returns:
        JSON: A list of Place objects associated with the specified City.
    """
    obj_city = storage.get(City, city_id)
    if not obj_city:
        abort(404)

    return jsonify([obj.to_dict() for obj in obj_city.places])


@app_views.route('/places/<place_id>', methods=['GET'], strict_slashes=False)
def single_place(place_id):
    """
    Retrieves details of a specific Place object.

    Args:
        place_id (str): The ID of the Place.

    Returns:
        JSON: Details of the specified Place object.
    """
    obj = storage.get(Place, place_id)
    if not obj:
        abort(404)
    return jsonify(obj.to_dict())


@app_views.route('/places/<place_id>',
                 methods=['DELETE'], strict_slashes=False)
def del_place(place_id):
    """
    Deletes a specific Place object.

    Args:
        place_id (str): The ID of the Place.

    Returns:
        JSON: An empty dictionary with the status code 200.
    """
    obj = storage.get(Place, place_id)
    if not obj:
        abort(404)
    obj.delete()
    storage.save()
    return make_response(jsonify({}), 200)


@app_views.route('cities/<city_id>/places',
                 methods=['POST'], strict_slashes=False)
def post_place(city_id):
    """
    Creates a new Place object associated with a specific City.

    Args:
        city_id (str): The ID of the City.

    Returns:
        JSON: Details of the new Place object with the status code 201.
    """
    obj_city = storage.get(City, city_id)
    if not obj_city:
        abort(404)

    new_place = request.get_json()
    if not new_place:
        abort(400, 'Not a JSON')
    if 'user_id' not in new_place:
        abort(400, "Missing user_id")
    user_id = new_place['user_id']
    obj_user = storage.get(User, user_id)
    if not obj_user:
        abort(404)
    if 'name' not in new_place:
        abort(400, "Missing name")

    # Create a new Place instance
    obj = Place(**new_place)
    setattr(obj, 'city_id', city_id)

    # Add the new Place to the storage
    storage.new(obj)
    storage.save()
    return make_response(jsonify(obj.to_dict()), 201)


@app_views.route('/places/<place_id>', methods=['PUT'], strict_slashes=False)
def put_place(place_id):
    """
    Updates details of a specific Place object.

    Args:
        place_id (str): The ID of the Place.

    Returns:
        JSON: Details of the updated Place object with the status code 200.
    """
    obj = storage.get(Place, place_id)
    if not obj:
        abort(404)

    req = request.get_json()
    if not req:
        abort(400, "Not a JSON")
