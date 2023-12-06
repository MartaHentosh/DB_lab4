from my_project.auth.dao import assigment_date_dao
from my_project.auth.service.general_service import GeneralService


class AssigmentDateService(GeneralService):
    """
    Realisation of Client service.
    """
    _dao = assigment_date_dao
