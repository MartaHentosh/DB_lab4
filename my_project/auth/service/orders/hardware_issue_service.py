from my_project.auth.dao import hardware_issue_dao
from my_project.auth.service.general_service import GeneralService


class HardwareIssueService(GeneralService):
    """
    Realisation of Client service.
    """
    _dao = hardware_issue_dao
