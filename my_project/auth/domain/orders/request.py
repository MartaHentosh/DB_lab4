from __future__ import annotations

from typing import Dict, Any

from my_project import db
from my_project.auth.domain.i_dto import IDto


class Request(db.Model, IDto):
    """
    Model declaration for Data Mapper.
    """
    __tablename__ = "request"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    request_type: str = db.Column(db.String(50))

    employee_id = db.Column(db.Integer, db.ForeignKey('employee.id'), nullable=False)
    employee = db.relationship('Employee', backref='requests', lazy=True)

    def __repr__(self) -> str:
        return f"Request({self.id}, {self.request_type})"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as a dictionary
        """
        return {
            "id": self.id,
            "request_type": self.request_type,
            "employee_info": f"{self.employee.phone_number} {self.employee.last_name}" if self.employee_id is not None else "",
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Request:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = Request(
            request_type=dto_dict.get("request_type"),
            employee_id=dto_dict.get("employee_id"),
        )
        return obj
