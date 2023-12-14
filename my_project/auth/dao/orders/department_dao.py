from typing import List

from my_project.auth.dao.general_dao import GeneralDAO

from my_project.auth.domain.orders.department import Department

from my_project.auth.domain.orders.department import employee_department

from my_project.auth.domain.orders.employee import Employee


class DepartmentDAO(GeneralDAO):
    """
    Realisation of Client data access layer.
    """
    _domain_type = Department

    def find_employees(self, department_id: int):
        """
        Find buses associated with a specific driver.
        :param department_id: ID of the driver
        :return: List of Bus objects associated with the driver
        """
        # Assuming that you have a session object, replace it with your actual SQLAlchemy session
        session = self.get_session()

        employee_ids = (
            session.query(employee_department.c.employee_id)
            .filter(employee_department.c.department_id == department_id)
            .all()
        )

        employee_ids = [employee_id for (employee_id,) in employee_ids]

        employees = session.query(Employee).filter(Employee.id.in_(employee_ids)).all()

        return [employee.put_into_dto() for employee in employees]

