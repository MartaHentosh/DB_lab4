
from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from my_project.auth.controller import employee_controller
from my_project.auth.domain import Employee

employee_bp = Blueprint('employee', __name__, url_prefix='/employees')


@employee_bp.get('')
def get_all_clients() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    return make_response(jsonify(employee_controller.find_all()), HTTPStatus.OK)

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


@employee_bp.get('/<int:employee_id>/departments')
def get_all_employees_from_departments(employee_id) -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    return make_response(jsonify(employee_controller.find_departments(employee_id)), HTTPStatus.OK)


@employee_bp.post('')
def create_client() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    content = request.get_json()
    employee = Employee.create_from_dto(content)
    employee_controller.create(employee)
    return make_response(jsonify(employee.put_into_dto()), HTTPStatus.CREATED)


@employee_bp.get('/<int:employee_id>')
def get_client(employee_id: int) -> Response:
    """
    Gets client by ID.
    :return: Response object
    """
    return make_response(jsonify(employee_controller.find_by_id(employee_id)), HTTPStatus.OK)


@employee_bp.put('/<int:employee_id>')
def update_client(employee_id: int) -> Response:
    """
    Updates client by ID.
    :return: Response object
    """
    content = request.get_json()
    employee = Employee.create_from_dto(content)
    employee_controller.update(employee_id, employee)
    return make_response("Employee updated", HTTPStatus.OK)


@employee_bp.patch('/<int:employee_id>')
def patch_client(employee_id: int) -> Response:
    """
    Patches client by ID.
    :return: Response object
    """
    content = request.get_json()
    employee_controller.patch(employee_id, content)
    return make_response("Employee updated", HTTPStatus.OK)


@employee_bp.delete('/<int:employee_id>')
def delete_client(employee_id: int) -> Response:
    """
    Deletes client by ID.
    :return: Response object
    """
    employee_controller.delete(employee_id)
    return make_response("Employee deleted", HTTPStatus.OK)
