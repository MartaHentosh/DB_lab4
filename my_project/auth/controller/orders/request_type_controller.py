from my_project.auth.controller.general_controller import GeneralController
from my_project.auth.service import request_type_service


class RequestTypeController(GeneralController):
    """
    Realisation of Client controller.
    """
    _service = request_type_service
