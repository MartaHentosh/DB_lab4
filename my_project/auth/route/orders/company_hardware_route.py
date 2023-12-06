
from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from my_project.auth.controller import company_hardware_controller
from my_project.auth.domain import CompanyHardware

company_hardware_bp = Blueprint('company_hardware', __name__, url_prefix='/company_hardwares')


@company_hardware_bp.get('')
def get_all_clients() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    return make_response(jsonify(company_hardware_controller.find_all()), HTTPStatus.OK)

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


@company_hardware_bp.post('')
def create_client() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    content = request.get_json()
    company_hardware = CompanyHardware.create_from_dto(content)
    company_hardware_controller.create(company_hardware)
    return make_response(jsonify(company_hardware.put_into_dto()), HTTPStatus.CREATED)


@company_hardware_bp.get('/<int:company_hardware_id>')
def get_client(company_hardware_id: int) -> Response:
    """
    Gets client by ID.
    :return: Response object
    """
    return make_response(jsonify(company_hardware_controller.find_by_id(company_hardware_id)), HTTPStatus.OK)


@company_hardware_bp.put('/<int:company_hardware_id>')
def update_client(company_hardware_id: int) -> Response:
    """
    Updates client by ID.
    :return: Response object
    """
    content = request.get_json()
    company_hardware = CompanyHardware.create_from_dto(content)
    company_hardware_controller.update(company_hardware_id, company_hardware)
    return make_response("CompanyHardware updated", HTTPStatus.OK)


@company_hardware_bp.patch('/<int:company_hardware_id>')
def patch_client(company_hardware_id: int) -> Response:
    """
    Patches client by ID.
    :return: Response object
    """
    content = request.get_json()
    company_hardware_controller.patch(company_hardware_id, content)
    return make_response("CompanyHardware updated", HTTPStatus.OK)


@company_hardware_bp.delete('/<int:company_hardware_id>')
def delete_client(company_hardware_id: int) -> Response:
    """
    Deletes client by ID.
    :return: Response object
    """
    company_hardware_controller.delete(company_hardware_id)
    return make_response("CompanyHardware deleted", HTTPStatus.OK)
