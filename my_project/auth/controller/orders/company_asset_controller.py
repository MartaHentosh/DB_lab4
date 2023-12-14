

from my_project.auth.controller.general_controller import GeneralController
from my_project.auth.service import company_asset_service


class CompanyAssetController(GeneralController):
    """
    Realisation of Client controller.
    """
    _service = company_asset_service
