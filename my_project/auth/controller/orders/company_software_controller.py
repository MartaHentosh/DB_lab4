from my_project.auth.controller.general_controller import GeneralController
from my_project.auth.service import company_software_service


class CompanySoftwareController(GeneralController):
    """
    Realisation of Client controller.
    """
    _service = company_software_service
