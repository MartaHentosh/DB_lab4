from my_project.auth.dao import company_asset_dao
from my_project.auth.service.general_service import GeneralService


class CompanyAssetService(GeneralService):
    """
    Realisation of Client service.
    """
    _dao = company_asset_dao

    def procedure_insert_into_company_asset(self, asset_name, asset_type,  employee_id, cost):
        return self._dao.procedure_insert_into_company_asset(asset_name, asset_type,  employee_id, cost)

    def make_operation(self, operation):
        return self._dao.make_operation(operation)

    def insert_data(self):
        return self._dao.insert_data()

    def create_tables_for_cursor(self):
        return self._dao.create_tables_for_cursor()
