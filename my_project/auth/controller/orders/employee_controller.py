from my_project.auth.controller.general_controller import GeneralController
from my_project.auth.service import employee_service


class EmployeeController(GeneralController):
    """
    Realisation of Client controller.
    """
    _service = employee_service

    def find_departments(self, employee_id: int):
        return self._service.find_departments(employee_id)

    def insert_employee_department_dependency(self, surname, departmentname):
        return self._service.insert_employee_department_dependency(surname, departmentname)
