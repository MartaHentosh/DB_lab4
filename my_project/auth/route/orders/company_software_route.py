
from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from my_project.auth.controller import company_software_controller
from my_project.auth.domain import CompanySoftware

company_software_bp = Blueprint('company_software', __name__, url_prefix='/company_softwares')


@company_software_bp.get('')
def get_all_clients() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    return make_response(jsonify(company_software_controller.find_all()), HTTPStatus.OK)

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


@company_software_bp.post('')
def create_client() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    content = request.get_json()
    company_software = CompanySoftware.create_from_dto(content)
    company_software_controller.create(company_software)
    return make_response(jsonify(company_software.put_into_dto()), HTTPStatus.CREATED)


@company_software_bp.get('/<int:company_software_id>')
def get_client(company_software_id: int) -> Response:
    """
    Gets client by ID.
    :return: Response object
    """
    return make_response(jsonify(company_software_controller.find_by_id(company_software_id)), HTTPStatus.OK)


@company_software_bp.put('/<int:company_software_id>')
def update_client(company_software_id: int) -> Response:
    """
    Updates client by ID.
    :return: Response object
    """
    content = request.get_json()
    company_software = CompanySoftware.create_from_dto(content)
    company_software_controller.update(company_software_id, company_software)
    return make_response("CompanySoftware updated", HTTPStatus.OK)


@company_software_bp.patch('/<int:company_software_id>')
def patch_client(company_software_id: int) -> Response:
    """
    Patches client by ID.
    :return: Response object
    """
    content = request.get_json()
    company_software_controller.patch(company_software_id, content)
    return make_response("CompanySoftware updated", HTTPStatus.OK)


@company_software_bp.delete('/<int:company_software_id>')
def delete_client(company_software_id: int) -> Response:
    """
    Deletes client by ID.
    :return: Response object
    """
    company_software_controller.delete(company_software_id)
    return make_response("CompanySoftware deleted", HTTPStatus.OK)
