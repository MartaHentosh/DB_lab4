
from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from my_project.auth.controller import request_controller
from my_project.auth.domain import Request

request_bp = Blueprint('request', __name__, url_prefix='/requests')


@request_bp.get('')
def get_all_clients() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    return make_response(jsonify(request_controller.find_all()), HTTPStatus.OK)

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


@request_bp.post('')
def create_client() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    content = request.get_json()
    request1 = Request.create_from_dto(content)
    request_controller.create(request1)
    return make_response(jsonify(request1.put_into_dto()), HTTPStatus.CREATED)


@request_bp.get('/<int:request_id>')
def get_client(request_id: int) -> Response:
    """
    Gets client by ID.
    :return: Response object
    """
    return make_response(jsonify(request_controller.find_by_id(request_id)), HTTPStatus.OK)


@request_bp.put('/<int:request_id>')
def update_client(request_id: int) -> Response:
    """
    Updates client by ID.
    :return: Response object
    """
    content = request.get_json()
    request1 = Request.create_from_dto(content)
    request_controller.update(request_id, request1)
    return make_response("Request updated", HTTPStatus.OK)


@request_bp.patch('/<int:request_id>')
def patch_client(request_id: int) -> Response:
    """
    Patches client by ID.
    :return: Response object
    """
    content = request.get_json()
    request_controller.patch(request_id, content)
    return make_response("Request updated", HTTPStatus.OK)


@request_bp.delete('/<int:request_id>')
def delete_client(request_id: int) -> Response:
    """
    Deletes client by ID.
    :return: Response object
    """
    request_controller.delete(request_id)
    return make_response("Request deleted", HTTPStatus.OK)
