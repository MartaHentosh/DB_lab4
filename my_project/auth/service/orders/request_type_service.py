from my_project.auth.dao import request_type_dao
from my_project.auth.service.general_service import GeneralService


class RequestTypeService(GeneralService):
    """
    Realisation of Client service.
    """
    _dao = request_type_dao
