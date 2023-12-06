from my_project.auth.controller.general_controller import GeneralController
from my_project.auth.service import request_service


class RequestController(GeneralController):
    """
    Realisation of Client controller.
    """
    _service = request_service
