

from my_project.auth.dao import department_dao
from my_project.auth.service.general_service import GeneralService


class DepartmentService(GeneralService):
    """
    Realisation of Client service.
    """
    _dao = department_dao
