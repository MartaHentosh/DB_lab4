from my_project.auth.dao import request_priority_dao
from my_project.auth.service.general_service import GeneralService


class RequestPriorityService(GeneralService):
    """
    Realisation of Client service.
    """
    _dao = request_priority_dao
