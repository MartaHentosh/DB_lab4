
from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from my_project.auth.controller import software_issue_controller
from my_project.auth.domain import SoftwareIssue

software_issue_bp = Blueprint('software_issue', __name__, url_prefix='/software_issues')


@software_issue_bp.get('')
def get_all_clients() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    return make_response(jsonify(software_issue_controller.find_all()), HTTPStatus.OK)

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


@software_issue_bp.post('')
def create_client() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    content = request.get_json()
    software_issue = SoftwareIssue.create_from_dto(content)
    software_issue_controller.create(software_issue)
    return make_response(jsonify(software_issue.put_into_dto()), HTTPStatus.CREATED)


@software_issue_bp.get('/<int:software_issue_id>')
def get_client(software_issue_id: int) -> Response:
    """
    Gets client by ID.
    :return: Response object
    """
    return make_response(jsonify(software_issue_controller.find_by_id(software_issue_id)), HTTPStatus.OK)


@software_issue_bp.put('/<int:software_issue_id>')
def update_client(software_issue_id: int) -> Response:
    """
    Updates client by ID.
    :return: Response object
    """
    content = request.get_json()
    software_issue = SoftwareIssue.create_from_dto(content)
    software_issue_controller.update(software_issue_id, software_issue)
    return make_response("SoftwareIssue updated", HTTPStatus.OK)


@software_issue_bp.patch('/<int:software_issue_id>')
def patch_client(software_issue_id: int) -> Response:
    """
    Patches client by ID.
    :return: Response object
    """
    content = request.get_json()
    software_issue_controller.patch(software_issue_id, content)
    return make_response("SoftwareIssue updated", HTTPStatus.OK)


@software_issue_bp.delete('/<int:software_issue_id>')
def delete_client(software_issue_id: int) -> Response:
    """
    Deletes client by ID.
    :return: Response object
    """
    software_issue_controller.delete(software_issue_id)
    return make_response("SoftwareIssue deleted", HTTPStatus.OK)
