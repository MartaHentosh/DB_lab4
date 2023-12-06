from my_project.auth.controller.general_controller import GeneralController
from my_project.auth.service import software_issue_service


class SoftwareIssueController(GeneralController):
    """
    Realisation of Client controller.
    """
    _service = software_issue_service
