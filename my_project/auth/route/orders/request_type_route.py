
from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from my_project.auth.controller import request_type_controller
from my_project.auth.domain import RequestType

request_type_bp = Blueprint('request_type', __name__, url_prefix='/request_types')


@request_type_bp.get('')
def get_all_clients() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    return make_response(jsonify(request_type_controller.find_all()), HTTPStatus.OK)

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


@request_type_bp.post('')
def create_client() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    content = request.get_json()
    request_type = RequestType.create_from_dto(content)
    request_type_controller.create(request_type)
    return make_response(jsonify(request_type.put_into_dto()), HTTPStatus.CREATED)


@request_type_bp.get('/<int:request_type_id>')
def get_client(request_type_id: int) -> Response:
    """
    Gets client by ID.
    :return: Response object
    """
    return make_response(jsonify(request_type_controller.find_by_id(request_type_id)), HTTPStatus.OK)


@request_type_bp.put('/<int:request_type_id>')
def update_client(request_type_id: int) -> Response:
    """
    Updates client by ID.
    :return: Response object
    """
    content = request.get_json()
    request_type = RequestType.create_from_dto(content)
    request_type_controller.update(request_type_id, request_type)
    return make_response("RequestType updated", HTTPStatus.OK)


@request_type_bp.patch('/<int:request_type_id>')
def patch_client(request_type_id: int) -> Response:
    """
    Patches client by ID.
    :return: Response object
    """
    content = request.get_json()
    request_type_controller.patch(request_type_id, content)
    return make_response("RequestType updated", HTTPStatus.OK)


@request_type_bp.delete('/<int:request_type_id>')
def delete_client(request_type_id: int) -> Response:
    """
    Deletes client by ID.
    :return: Response object
    """
    request_type_controller.delete(request_type_id)
    return make_response("RequestType deleted", HTTPStatus.OK)
