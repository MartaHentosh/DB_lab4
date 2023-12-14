from typing import List

from my_project.auth.dao.general_dao import GeneralDAO

from my_project.auth.domain.orders.employee import Employee

from my_project.auth.domain.orders.department import employee_department
from my_project.auth.domain.orders.department import Department


class EmployeeDAO(GeneralDAO):
    """
    Realisation of Client data access layer.
    """
    _domain_type = Employee

    def find_departments(self, employee_id: int):
        """
        Find buses associated with a specific driver=movie.
        :param employee_id: ID of the driver
        :return: List of Bus objects associated with the driver
        """
        session = self.get_session()

        department_ids = (
            session.query(employee_department.c.department_id)
            .filter(employee_department.c.employee_id == employee_id)
            .all()
        )

        department_ids = [department_id for (department_id,) in department_ids]

        departments = session.query(Department).filter(Department.id.in_(department_ids)).all()

        return [department.put_into_dto() for department in departments]
