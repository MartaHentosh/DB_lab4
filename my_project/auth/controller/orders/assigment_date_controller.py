from my_project.auth.controller.general_controller import GeneralController
from my_project.auth.service import assigment_date_service


class AssigmentDateController(GeneralController):
    """
    Realisation of Client controller.
    """
    _service = assigment_date_service
