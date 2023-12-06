
from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from my_project.auth.controller import assigment_date_controller
from my_project.auth.domain import AssigmentDate

assigment_date_bp = Blueprint('assigment_date', __name__, url_prefix='/assigment_dates')


@assigment_date_bp.get('')
def get_all_clients() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    return make_response(jsonify(assigment_date_controller.find_all()), HTTPStatus.OK)

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


@assigment_date_bp.post('')
def create_client() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    content = request.get_json()
    assigment_date = AssigmentDate.create_from_dto(content)
    assigment_date_controller.create(assigment_date)
    return make_response(jsonify(assigment_date.put_into_dto()), HTTPStatus.CREATED)


@assigment_date_bp.get('/<int:assigment_date_id>')
def get_client(assigment_date_id: int) -> Response:
    """
    Gets client by ID.
    :return: Response object
    """
    return make_response(jsonify(assigment_date_controller.find_by_id(assigment_date_id)), HTTPStatus.OK)


@assigment_date_bp.put('/<int:assigment_date_id>')
def update_client(assigment_date_id: int) -> Response:
    """
    Updates client by ID.
    :return: Response object
    """
    content = request.get_json()
    assigment_date = AssigmentDate.create_from_dto(content)
    assigment_date_controller.update(assigment_date_id, assigment_date)
    return make_response("AssigmentDate updated", HTTPStatus.OK)


@assigment_date_bp.patch('/<int:assigment_date_id>')
def patch_client(assigment_date_id: int) -> Response:
    """
    Patches client by ID.
    :return: Response object
    """
    content = request.get_json()
    assigment_date_controller.patch(assigment_date_id, content)
    return make_response("AssigmentDate updated", HTTPStatus.OK)


@assigment_date_bp.delete('/<int:assigment_date_id>')
def delete_client(assigment_date_id: int) -> Response:
    """
    Deletes client by ID.
    :return: Response object
    """
    assigment_date_controller.delete(assigment_date_id)
    return make_response("AssigmentDate deleted", HTTPStatus.OK)
