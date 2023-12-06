from my_project.auth.controller.general_controller import GeneralController
from my_project.auth.service import company_hardware_service


class CompanyHardwareController(GeneralController):
    """
    Realisation of Client controller.
    """
    _service = company_hardware_service
