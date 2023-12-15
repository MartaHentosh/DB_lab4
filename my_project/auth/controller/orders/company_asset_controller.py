
from my_project.auth.controller.general_controller import GeneralController
from my_project.auth.service import company_asset_service


class CompanyAssetController(GeneralController):
    """
    Realisation of Client controller.
    """
    _service = company_asset_service

    def procedure_insert_into_company_asset(self, asset_name, asset_type, employee_id, cost):
        self._service.procedure_insert_into_company_asset(asset_name, asset_type, employee_id, cost)

    def make_operation(self, operation):
        return self._service.make_operation(operation)

    def insert_data(self):
        return self._service.insert_data()

    def create_tables_for_cursor(self):
        return self._service.create_tables_for_cursor()
