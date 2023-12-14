
from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from my_project.auth.controller import company_asset_controller
from my_project.auth.domain import CompanyAsset

company_asset_bp = Blueprint('company_asset', __name__, url_prefix='/company_assets')


@company_asset_bp.get('')
def get_all_clients() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    return make_response(jsonify(company_asset_controller.find_all()), HTTPStatus.OK)


@company_asset_bp.post('')
def create_client() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    content = request.get_json()
    company_asset = CompanyAsset.create_from_dto(content)
    company_asset_controller.create(company_asset)
    return make_response(jsonify(company_asset.put_into_dto()), HTTPStatus.CREATED)


@company_asset_bp.get('/<int:company_asset_id>')
def get_client(company_asset_id: int) -> Response:
    """
    Gets client by ID.
    :return: Response object
    """
    return make_response(jsonify(company_asset_controller.find_by_id(company_asset_id)), HTTPStatus.OK)


@company_asset_bp.put('/<int:company_asset_id>')
def update_client(company_asset_id: int) -> Response:
    """
    Updates client by ID.
    :return: Response object
    """
    content = request.get_json()
    company_asset = CompanyAsset.create_from_dto(content)
    company_asset_controller.update(company_asset_id, company_asset)
    return make_response("CompanyAsset updated", HTTPStatus.OK)


@company_asset_bp.patch('/<int:company_asset_id>')
def patch_client(company_asset_id: int) -> Response:
    """
    Patches client by ID.
    :return: Response object
    """
    content = request.get_json()
    company_asset_controller.patch(company_asset_id, content)
    return make_response("CompanyAsset updated", HTTPStatus.OK)


@company_asset_bp.delete('/<int:department_id>')
def delete_client(department_id: int) -> Response:
    """
    Deletes client by ID.
    :return: Response object
    """
    department_controller.delete(department_id)
    return make_response("Department deleted", HTTPStatus.OK)
