

from my_project.auth.controller.general_controller import GeneralController
from my_project.auth.service import department_service


class DepartmentController(GeneralController):
    """
    Realisation of Client controller.
    """
    _service = department_service
