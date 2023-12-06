from my_project.auth.dao import software_issue_dao
from my_project.auth.service.general_service import GeneralService


class SoftwareIssueService(GeneralService):
    """
    Realisation of Client service.
    """
    _dao = software_issue_dao
