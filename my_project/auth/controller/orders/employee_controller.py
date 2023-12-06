from my_project.auth.controller.general_controller import GeneralController
from my_project.auth.service import employee_service


class EmployeeController(GeneralController):
    """
    Realisation of Client controller.
    """
    _service = employee_service
