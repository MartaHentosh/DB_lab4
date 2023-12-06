from my_project.auth.dao import request_dao
from my_project.auth.service.general_service import GeneralService


class RequestService(GeneralService):
    """
    Realisation of Client service.
    """
    _dao = request_dao
