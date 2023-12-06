from my_project.auth.controller.general_controller import GeneralController
from my_project.auth.service import request_status_service


class RequestStatusController(GeneralController):
    """
    Realisation of Client controller.
    """
    _service = request_status_service
