#!/usr/bin/python3
'''Cities API View'''

from flask import abort, jsonify, make_response, request
from api.v1.views import app_views
from models import storage
from models.city import City
from models.state import State


@app_views.route('/states/<state_id>/cities',
                 methods=['GET'], strict_slashes=False)
def cities(state_id):
    """
    Retrieves the list of all City objects of a State.

    Args:
        state_id (str): The ID of the State.

    Returns:
        JSON: A list of City objects associated with the specified State.
    """
    obj_state = storage.get(State, state_id)
    if not obj_state:
        abort(404)
    return jsonify([city.to_dict() for city in obj_state.cities])


@app_views.route('/cities/<city_id>', methods=['GET'], strict_slashes=False)
def single_city(city_id):
    """
    Retrieves details of a specific City object.

    Args:
        city_id (str): The ID of the City.

    Returns:
        JSON: Details of the specified City object.
    """
    obj = storage.get(City, city_id)
    if not obj:
        abort(404)
    return jsonify(obj.to_dict())


@app_views.route('/cities/<city_id>', methods=['DELETE'], strict_slashes=False)
def del_city(city_id):
    """
    Deletes a specific City object.

    Args:
        city_id (str): The ID of the City.

    Returns:
        JSON: An empty dictionary with the status code 200.
    """
    obj = storage.get(City, city_id)
    if not obj:
        abort(404)
    obj.delete()
    storage.save()
    return make_response(jsonify({}), 200)


@app_views.route('/states/<state_id>/cities',
                 methods=['POST'], strict_slashes=False)
def post_city(state_id):
    """
    Creates a new City object associated with a specific State.

    Args:
        state_id (str): The ID of the State.

    Returns:
        JSON: Details of the new City object with the status code 201.
    """
    obj_state = storage.get(State, state_id)
    if not obj_state:
        abort(404)

    new_city = request.get_json()
    if not new_city:
        abort(400, "Invalid JSON format")
    if 'name' not in new_city:
        abort(400, "Missing 'name' attribute")

    # Create a new City instance
    obj = City(**new_city)
    setattr(obj, 'state_id', state_id)

    # Add the new City to the storage
    storage.new(obj)
    storage.save()

    return make_response(jsonify(obj.to_dict()), 201)


@app_views.route('/cities/<city_id>', methods=['PUT'], strict_slashes=False)
def put_city(city_id):
    """
    Updates details of a specific City object.

    Args:
        city_id (str): The ID of the City.

    Returns:
        JSON: Details of the updated City object with the status code 200.
    """
    obj = storage.get(City, city_id)
    if not obj:
        abort(404)

    req = request.get_json()
    if not req:
        abort(400, "Invalid JSON format")

    # Update City attributes based on the request
    for k, v in req.items():
        if k not in ['id', 'created_at', 'update_at', 'state_id']:
            setattr(obj, k, v)

    # Save the changes to storage
    storage.save()
    
    return make_response(jsonify(obj.to_dict()), 200)
