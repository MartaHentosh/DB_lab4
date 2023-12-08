from __future__ import annotations

from typing import Dict, Any

from my_project import db
from my_project.auth.domain.i_dto import IDto

from my_project.auth.domain.orders.department import employee_department


class Employee(db.Model, IDto):
    """
    Model declaration for Data Mapper.
    """
    __tablename__ = "employee"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name: str = db.Column(db.String(45))
    last_name: str = db.Column(db.String(45))
    email: str = db.Column(db.String(45))
    phone_number: str = db.Column(db.String(15))

    # Many-to-Many relationship with Department
    departments = db.relationship('Department', secondary=employee_department)

    def __repr__(self) -> str:
        return f"Employee({self.id}, {self.first_name}, {self.last_name}, {self.email})"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as a dictionary
        """
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
            "phone_number": self.phone_number,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Employee:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = Employee(
            first_name=dto_dict.get("first_name"),
            last_name=dto_dict.get("last_name"),
            email=dto_dict.get("email"),
            phone_number=dto_dict.get("phone_number"),
        )
        return obj
