
from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from my_project.auth.controller import hardware_issue_controller
from my_project.auth.domain import HardwareIssue

hardware_issue_bp = Blueprint('hardware_issue', __name__, url_prefix='/hardware_issues')


@hardware_issue_bp.get('')
def get_all_clients() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    return make_response(jsonify(hardware_issue_controller.find_all()), HTTPStatus.OK)

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


@hardware_issue_bp.post('')
def create_client() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    content = request.get_json()
    hardware_issue = HardwareIssue.create_from_dto(content)
    hardware_issue_controller.create(hardware_issue)
    return make_response(jsonify(hardware_issue.put_into_dto()), HTTPStatus.CREATED)


@hardware_issue_bp.get('/<int:hardware_issue_id>')
def get_client(hardware_issue_id: int) -> Response:
    """
    Gets client by ID.
    :return: Response object
    """
    return make_response(jsonify(hardware_issue_controller.find_by_id(hardware_issue_id)), HTTPStatus.OK)


@hardware_issue_bp.put('/<int:hardware_issue_id>')
def update_client(hardware_issue_id: int) -> Response:
    """
    Updates client by ID.
    :return: Response object
    """
    content = request.get_json()
    hardware_issue = HardwareIssue.create_from_dto(content)
    hardware_issue_controller.update(hardware_issue_id, hardware_issue)
    return make_response("HardwareIssue updated", HTTPStatus.OK)


@hardware_issue_bp.patch('/<int:hardware_issue_id>')
def patch_client(hardware_issue_id: int) -> Response:
    """
    Patches client by ID.
    :return: Response object
    """
    content = request.get_json()
    hardware_issue_controller.patch(hardware_issue_id, content)
    return make_response("HardwareIssue updated", HTTPStatus.OK)


@hardware_issue_bp.delete('/<int:hardware_issue_id>')
def delete_client(hardware_issue_id: int) -> Response:
    """
    Deletes client by ID.
    :return: Response object
    """
    hardware_issue_controller.delete(hardware_issue_id)
    return make_response("HardwareIssue deleted", HTTPStatus.OK)
