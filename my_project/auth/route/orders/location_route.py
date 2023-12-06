
from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from my_project.auth.controller import location_controller
from my_project.auth.domain import Location

location_bp = Blueprint('location', __name__, url_prefix='/locations')


@location_bp.get('')
def get_all_clients() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    return make_response(jsonify(location_controller.find_all()), HTTPStatus.OK)

# @department_bp.get('/<int:department_id>/depatments')
# def get_all_buses_from_drivers(bus_id) -> Response:
#     """
#     Gets all objects from table using Service layer.
#     :return: Response object
#     """
#     return make_response(jsonify(bus_controller.find_drivers(bus_id)), HTTPStatus.OK)
#
# @department_bp.get('/<int:bus_id>/routes')
# def get_all_buses_from_routes(bus_id) -> Response:
#     """
#     Gets all objects from table using Service layer.
#     :return: Response object
#     """
#     return make_response(jsonify(bus_controller.find_routes(bus_id)), HTTPStatus.OK)


@location_bp.post('')
def create_client() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    content = request.get_json()
    location = Location.create_from_dto(content)
    location_controller.create(location)
    return make_response(jsonify(location.put_into_dto()), HTTPStatus.CREATED)


@location_bp.get('/<int:location_id>')
def get_client(location_id: int) -> Response:
    """
    Gets client by ID.
    :return: Response object
    """
    return make_response(jsonify(location_controller.find_by_id(location_id)), HTTPStatus.OK)


@location_bp.put('/<int:location_id>')
def update_client(location_id: int) -> Response:
    """
    Updates client by ID.
    :return: Response object
    """
    content = request.get_json()
    location = Location.create_from_dto(content)
    location_controller.update(location_id, location)
    return make_response("Location updated", HTTPStatus.OK)


@location_bp.patch('/<int:location_id>')
def patch_client(location_id: int) -> Response:
    """
    Patches client by ID.
    :return: Response object
    """
    content = request.get_json()
    location_controller.patch(location_id, content)
    return make_response("Location updated", HTTPStatus.OK)


@location_bp.delete('/<int:location_id>')
def delete_client(location_id: int) -> Response:
    """
    Deletes client by ID.
    :return: Response object
    """
    location_controller.delete(location_id)
    return make_response("Location deleted", HTTPStatus.OK)
