
from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from my_project.auth.controller import department_controller
from my_project.auth.domain import Department

department_bp = Blueprint('department', __name__, url_prefix='/departments')


@department_bp.get('')
def get_all_clients() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    return make_response(jsonify(department_controller.find_all()), HTTPStatus.OK)

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


@department_bp.post('')
def create_client() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    content = request.get_json()
    department = Department.create_from_dto(content)
    department_controller.create(department)
    return make_response(jsonify(department.put_into_dto()), HTTPStatus.CREATED)


@department_bp.get('/<int:department_id>')
def get_client(department_id: int) -> Response:
    """
    Gets client by ID.
    :return: Response object
    """
    return make_response(jsonify(department_controller.find_by_id(department_id)), HTTPStatus.OK)


@department_bp.put('/<int:department_id>')
def update_client(department_id: int) -> Response:
    """
    Updates client by ID.
    :return: Response object
    """
    content = request.get_json()
    department = Department.create_from_dto(content)
    department_controller.update(department_id, department)
    return make_response("Department updated", HTTPStatus.OK)


@department_bp.patch('/<int:department_id>')
def patch_client(department_id: int) -> Response:
    """
    Patches client by ID.
    :return: Response object
    """
    content = request.get_json()
    department_controller.patch(department_id, content)
    return make_response("Department updated", HTTPStatus.OK)


@department_bp.delete('/<int:department_id>')
def delete_client(department_id: int) -> Response:
    """
    Deletes client by ID.
    :return: Response object
    """
    department_controller.delete(department_id)
    return make_response("Department deleted", HTTPStatus.OK)
