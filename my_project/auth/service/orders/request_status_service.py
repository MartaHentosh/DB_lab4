from my_project.auth.dao import request_status_dao
from my_project.auth.service.general_service import GeneralService


class RequestStatusService(GeneralService):
    """
    Realisation of Client service.
    """
    _dao = request_status_dao
