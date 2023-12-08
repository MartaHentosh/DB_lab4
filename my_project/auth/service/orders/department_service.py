from my_project.auth.dao import department_dao
from my_project.auth.service.general_service import GeneralService


class DepartmentService(GeneralService):
    """
    Realisation of Client service.
    """
    _dao = department_dao

    def find_employees(self, department_id: int):
        return self._dao.find_employees(department_id)
