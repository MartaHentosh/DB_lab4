
from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from my_project.auth.controller import request_priority_controller
from my_project.auth.domain import RequestPriority

request_priority_bp = Blueprint('request_priority', __name__, url_prefix='/request_priorities')


@request_priority_bp.get('')
def get_all_clients() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    return make_response(jsonify(request_priority_controller.find_all()), HTTPStatus.OK)

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


@request_priority_bp.post('')
def create_client() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    content = request.get_json()
    request_priority = RequestPriority.create_from_dto(content)
    request_priority_controller.create(request_priority)
    return make_response(jsonify(request_priority.put_into_dto()), HTTPStatus.CREATED)


@request_priority_bp.get('/<int:request_priority_id>')
def get_client(request_priority_id: int) -> Response:
    """
    Gets client by ID.
    :return: Response object
    """
    return make_response(jsonify(request_priority_controller.find_by_id(request_priority_id)), HTTPStatus.OK)


@request_priority_bp.put('/<int:request_priority_id>')
def update_client(request_priority_id: int) -> Response:
    """
    Updates client by ID.
    :return: Response object
    """
    content = request.get_json()
    request_priority = RequestPriority.create_from_dto(content)
    request_priority_controller.update(request_priority_id, request_priority)
    return make_response("RequestPriority updated", HTTPStatus.OK)


@request_priority_bp.patch('/<int:request_priority_id>')
def patch_client(request_priority_id: int) -> Response:
    """
    Patches client by ID.
    :return: Response object
    """
    content = request.get_json()
    request_priority_controller.patch(request_priority_id, content)
    return make_response("RequestPriority updated", HTTPStatus.OK)


@request_priority_bp.delete('/<int:request_priority_id>')
def delete_client(request_priority_id: int) -> Response:
    """
    Deletes client by ID.
    :return: Response object
    """
    request_priority_controller.delete(request_priority_id)
    return make_response("RequestPriority deleted", HTTPStatus.OK)
