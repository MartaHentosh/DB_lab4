from my_project.auth.controller.general_controller import GeneralController
from my_project.auth.service import request_priority_service


class RequestPriorityController(GeneralController):
    """
    Realisation of Client controller.
    """
    _service = request_priority_service
