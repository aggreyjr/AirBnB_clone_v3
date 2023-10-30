#!/usr/bin/python3
'''States API View'''

from flask import abort, jsonify, make_response, request
from api.v1.views import app_views
from models import storage
from models.state import State


@app_views.route('/states', methods=['GET'], strict_slashes=False)
def state():
    """
    Retrieves the list of all State objects.

    Returns:
        JSON: A list of State objects.
    """
    objs = storage.all(State)
    return jsonify([obj.to_dict() for obj in objs.values()])


@app_views.route('/states/<state_id>', methods=['GET'], strict_slashes=False)
def single_state(state_id):
    """
    Retrieves details of a specific State object.

    Args:
        state_id (str): The ID of the State.

    Returns:
        JSON: Details of the specified State object.
    """
    obj = storage.get(State, state_id)
    if not obj:
        abort(404)
    return jsonify(obj.to_dict())


@app_views.route('/states/<state_id>',
                 methods=['DELETE'], strict_slashes=False)
def del_state(state_id):
    """
    Deletes a specific State object.

    Args:
        state_id (str): The ID of the State.

    Returns:
        JSON: An empty dictionary with the status code 200.
    """
    obj = storage.get(State, state_id)
    if not obj:
        abort(404)
    obj.delete()
    storage.save()
    return make_response(jsonify({}), 200)


@app_views.route('/states', methods=['POST'], strict_slashes=False)
def post_state():
    """
    Creates a new State object.

    Returns:
        JSON: Details of the new State object with the status code 201.
    """
    new_obj = request.get_json()
    if not new_obj:
        abort(400, "Invalid JSON format")
    if 'name' not in new_obj:
        abort(400, "Missing 'name' attribute")

    # Create a new State instance
    obj = State(**new_obj)

    # Add the new State to the storage
    storage.new(obj)
    storage.save()
    return make_response(jsonify(obj.to_dict()), 201)


@app_views.route('/states/<state_id>', methods=['PUT'], strict_slashes=False)
def put_state(state_id):
    """
    Updates details of a specific State object.

    Args:
        state_id (str): The ID of the State.

    Returns:
        JSON: Details of the updated State object with the status code 200.
    """
    obj = storage.get(State, state_id)
    if not obj:
        abort(404)

    req = request.get_json()
    if not req:
        abort(400, "Invalid JSON format")

    # Update State attributes based on the request
    for k, v in req.items():
        if k not in ['id', 'created_at', 'updated_at']:
            setattr(obj, k, v)

    # Save the changes to storage
    storage.save()
    
    return make_response(jsonify(obj.to_dict()), 200)
