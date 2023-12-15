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


@company_asset_bp.delete('/<int:company_asset_id>')
def delete_client(company_asset_id: int) -> Response:
    """
    Deletes client by ID.
    :return: Response object
    """
    company_asset_controller.delete(company_asset_id)
    return make_response("Department deleted", HTTPStatus.OK)


@company_asset_bp.post('/asset_name/<string:asset_name>/asset_type/<string:asset_type>/'
                       'employee_id/<int:employee_id>/cost/<float:cost>')
def insert_into_company_asset(asset_name, asset_type, employee_id, cost) -> Response:
    company_asset_controller.procedure_insert_into_company_asset(asset_name, asset_type, employee_id, cost)
    response_data = {'message': 'Insert added successfully'}
    return make_response(response_data, HTTPStatus.CREATED)


@company_asset_bp.get('/operation/<string:operation>')
def get_operation_on_products(operation) -> Response:
    result = company_asset_controller.make_operation(operation)
    return make_response(jsonify({
        f"{operation}": result
    }), HTTPStatus.OK)


@company_asset_bp.post('/data')
def insert_data() -> Response:
    company_asset_controller.insert_data()
    return make_response("Products inserted successfully")


@company_asset_bp.post('/table')
def create_tables_for_cursor() -> Response:
    result = company_asset_controller.create_tables_for_cursor()
    response = {"result": f"{result}, Table created successfully"}
    return make_response(jsonify(response), HTTPStatus.CREATED)
