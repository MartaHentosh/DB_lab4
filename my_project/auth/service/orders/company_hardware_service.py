from my_project.auth.dao import company_hardware_dao
from my_project.auth.service.general_service import GeneralService


class CompanyHardwareService(GeneralService):
    """
    Realisation of Client service.
    """
    _dao = company_hardware_dao
