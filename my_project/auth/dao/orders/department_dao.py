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

        # Query the association table to get the bus IDs associated with the driver
        employee_ids = (
            session.query(employee_department.c.employee_id)
            .filter(employee_department.c.department_id == department_id)
            .all()
        )

        # Extract bus IDs from the result
        employee_ids = [employee_id for (employee_id,) in employee_ids]

        # Query the Bus table to get the Bus objects associated with the bus IDs
        employees = session.query(Employee).filter(Employee.id.in_(employee_ids)).all()

        return [employee.put_into_dto() for employee in employees]

    # def find_routes(self, bus_id: int):
    #     """
    #     Find buses associated with a specific driver.
    #     :param bus_id: ID of the driver
    #     :return: List of Bus objects associated with the driver
    #     """
    #     # Assuming that you have a session object, replace it with your actual SQLAlchemy session
    #     session = self.get_session()
    #
    #     # Query the association table to get the bus IDs associated with the driver
    #     route_ids = (
    #         session.query(route_bus.c.route_id)
    #         .filter(route_bus.c.bus_id == bus_id)
    #         .all()
    #     )
    #
    #     # Extract bus IDs from the result
    #     route_ids = [route_id for (route_id,) in route_ids]
    #
    #     # Query the Bus table to get the Bus objects associated with the bus IDs
    #     routes = session.query(Route).filter(Route.id.in_(route_ids)).all()
    #
    #     return [route.put_into_dto() for route in routes]
