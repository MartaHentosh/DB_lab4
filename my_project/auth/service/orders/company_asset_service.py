from my_project.auth.dao import company_asset_dao
from my_project.auth.service.general_service import GeneralService


class CompanyAssetService(GeneralService):
    """
    Realisation of Client service.
    """
    _dao = company_asset_dao
