from my_project.auth.dao import company_software_dao
from my_project.auth.service.general_service import GeneralService


class CompanySoftwareService(GeneralService):
    """
    Realisation of Client service.
    """
    _dao = company_software_dao
