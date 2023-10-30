#!/usr/bin/python3
<<<<<<< HEAD
"""states.py"""

from api.v1.views import app_views
from flask import abort, jsonify, make_response, request
=======
'''Amenities API View'''

from flask import abort, jsonify, make_response, request
from api.v1.views import app_views
>>>>>>> f882f28fbb4bc1cce89dbfba741a0f92c9394176
from models import storage
from models.amenity import Amenity


@app_views.route('/amenities', methods=['GET'], strict_slashes=False)
<<<<<<< HEAD
def get_amenities():
    """get amenity information for all amenities"""
    amenities = []
    for amenity in storage.all("Amenity").values():
        amenities.append(amenity.to_dict())
    return jsonify(amenities)


@app_views.route('/amenities/<string:amenity_id>', methods=['GET'],
                 strict_slashes=False)
def get_amenity(amenity_id):
    """get amenity information for specified amenity"""
    amenity = storage.get("Amenity", amenity_id)
    if amenity is None:
        abort(404)
    return jsonify(amenity.to_dict())


@app_views.route('/amenities/<string:amenity_id>', methods=['DELETE'],
                 strict_slashes=False)
def delete_amenity(amenity_id):
    """deletes an amenity based on its amenity_id"""
    amenity = storage.get("Amenity", amenity_id)
    if amenity is None:
        abort(404)
    amenity.delete()
    storage.save()
    return (jsonify({}))
=======
def amenities():
    """
    Retrieves the list of all Amenity objects.

    Returns:
        JSON: A list of Amenity objects.
    """
    objs = storage.all(Amenity)
    return jsonify([obj.to_dict() for obj in objs.values()])


@app_views.route('/amenities/<amenity_id>',
                 methods=['GET'], strict_slashes=False)
def single_amenities(amenity_id):
    """
    Retrieves a specific Amenity object.

    Args:
        amenity_id (str): The ID of the Amenity.

    Returns:
        JSON: Details of the Amenity object.
    """
    obj = storage.get(Amenity, amenity_id)
    if not obj:
        abort(404)
    return jsonify(obj.to_dict())


@app_views.route('/amenities/<amenity_id>',
                 methods=['DELETE'], strict_slashes=False)
def del_amenities(amenity_id):
    """
    Deletes a specific Amenity object.

    Args:
        amenity_id (str): The ID of the Amenity.

    Returns:
        JSON: An empty dictionary with the status code 200.
    """
    obj = storage.get(Amenity, amenity_id)
    if not obj:
        abort(404)

    obj.delete()
    storage.save()
    return make_response(jsonify({}), 200)
>>>>>>> f882f28fbb4bc1cce89dbfba741a0f92c9394176


@app_views.route('/amenities', methods=['POST'], strict_slashes=False)
def post_amenity():
<<<<<<< HEAD
    """create a new amenity"""
    if not request.get_json():
        return make_response(jsonify({'error': 'Not a JSON'}), 400)
    if 'name' not in request.get_json():
        return make_response(jsonify({'error': 'Missing name'}), 400)
    amenity = Amenity(**request.get_json())
    amenity.save()
    return make_response(jsonify(amenity.to_dict()), 201)


@app_views.route('/amenities/<string:amenity_id>', methods=['PUT'],
                 strict_slashes=False)
def put_amenity(amenity_id):
    """update an amenity"""
    amenity = storage.get("Amenity", amenity_id)
    if amenity is None:
        abort(404)
    if not request.get_json():
        return make_response(jsonify({'error': 'Not a JSON'}), 400)
    for attr, val in request.get_json().items():
        if attr not in ['id', 'created_at', 'updated_at']:
            setattr(amenity, attr, val)
    amenity.save()
    return jsonify(amenity.to_dict())
=======
    """
    Creates a new Amenity object.

    Returns:
        JSON: Details of the new Amenity object with the status code 201.
    """
    new_amenity = request.get_json()
    if not new_amenity:
        abort(400, "Invalid JSON format")
    if 'name' not in new_amenity:
        abort(400, "Missing 'name' attribute")

    # Create a new Amenity instance
    obj = Amenity(**new_amenity)

    # Add the new Amenity to the storage
    storage.new(obj)
    storage.save()

    return make_response(jsonify(obj.to_dict()), 201)


@app_views.route('/amenities/<amenity_id>',
                 methods=['PUT'], strict_slashes=False)
def put_amenity(amenity_id):
    """
    Updates a specific Amenity object.

    Args:
        amenity_id (str): The ID of the Amenity.

    Returns:
        JSON: Details of the updated Amenity object with the status code 200.
    """
    obj = storage.get(Amenity, amenity_id)
    if not obj:
        abort(404)

    req = request.get_json()
    if not req:
        abort(400, "Invalid JSON format")

    # Update Amenity attributes based on the request
    for k, v in req.items():
        if k not in ['id', 'created_at', 'update_at']:
            setattr(obj, k, v)

    # Save the changes to storage
    storage.save()
    
    return make_response(jsonify(obj.to_dict()), 200)
>>>>>>> f882f28fbb4bc1cce89dbfba741a0f92c9394176
