from my_project.auth.dao import employee_dao
from my_project.auth.service.general_service import GeneralService


class EmployeeService(GeneralService):
    """
    Realisation of Client service.
    """
    _dao = employee_dao

    def find_departments(self, employee_id: int):
        return self._dao.find_departments(employee_id)

    def insert_employee_department_dependency(self, surname, departmentname):
        return self._dao.insert_employee_department_dependency(surname, departmentname)
