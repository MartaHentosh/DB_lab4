
from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from my_project.auth.controller import request_status_controller
from my_project.auth.domain import RequestStatus

request_status_bp = Blueprint('request_status', __name__, url_prefix='/request_statuses')


@request_status_bp.get('')
def get_all_clients() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    return make_response(jsonify(request_status_controller.find_all()), HTTPStatus.OK)

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


@request_status_bp.post('')
def create_client() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    content = request.get_json()
    request_status = RequestStatus.create_from_dto(content)
    request_status_controller.create(request_status)
    return make_response(jsonify(request_status.put_into_dto()), HTTPStatus.CREATED)


@request_status_bp.get('/<int:request_status_id>')
def get_client(request_status_id: int) -> Response:
    """
    Gets client by ID.
    :return: Response object
    """
    return make_response(jsonify(request_status_controller.find_by_id(request_status_id)), HTTPStatus.OK)


@request_status_bp.put('/<int:request_status_id>')
def update_client(request_status_id: int) -> Response:
    """
    Updates client by ID.
    :return: Response object
    """
    content = request.get_json()
    request_status = RequestStatus.create_from_dto(content)
    request_status_controller.update(request_status_id, request_status)
    return make_response("RequestStatus updated", HTTPStatus.OK)


@request_status_bp.patch('/<int:request_status_id>')
def patch_client(request_status_id: int) -> Response:
    """
    Patches client by ID.
    :return: Response object
    """
    content = request.get_json()
    request_status_controller.patch(request_status_id, content)
    return make_response("RequestStatus updated", HTTPStatus.OK)


@request_status_bp.delete('/<int:request_status_id>')
def delete_client(request_status_id: int) -> Response:
    """
    Deletes client by ID.
    :return: Response object
    """
    request_status_controller.delete(request_status_id)
    return make_response("RequestStatus deleted", HTTPStatus.OK)
