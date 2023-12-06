from my_project.auth.controller.general_controller import GeneralController
from my_project.auth.service import hardware_issue_service


class HardwareIssueController(GeneralController):
    """
    Realisation of Client controller.
    """
    _service = hardware_issue_service
