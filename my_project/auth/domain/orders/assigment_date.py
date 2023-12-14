from __future__ import annotations

from typing import Dict, Any

from my_project import db
from my_project.auth.domain.i_dto import IDto


class AssigmentDate(db.Model, IDto):
    """
    Model declaration for Data Mapper.
    """
    __tablename__ = "assigment_date"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    date_time = db.Column(db.Date)

    request_id = db.Column(db.Integer, db.ForeignKey('request.id'), nullable=False)
    request = db.relationship('Request', backref='request', lazy=True)

    employee_id = db.Column(db.Integer, db.ForeignKey('employee.id'), nullable=False)
    employee = db.relationship('Employee', backref='employee', lazy=True)

    def __repr__(self) -> str:
        return f"AssigmentDate({self.id}, {self.date_time})"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as a dictionary
        """
        return {
            "id": self.id,
            "date_time": self.date_time,
            "request_type": self.request.request_type if self.request_id is not None else "",
            "employee_name": f"{self.employee.first_name} {self.employee.last_name}" if self.employee_id is not None else "",
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> AssigmentDate:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = AssigmentDate(
            date_time=dto_dict.get("date_time"),
            request_id=dto_dict.get("request_id"),
            employee_id=dto_dict.get("employee_id"),
        )
        return obj
