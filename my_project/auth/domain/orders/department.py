from __future__ import annotations

from typing import Dict, Any

from my_project import db
from my_project.auth.domain.i_dto import IDto


class Department(db.Model, IDto):
    """
    Model declaration for Data Mapper.
    """
    __tablename__ = "department"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name_dapartment: str = db.Column(db.String(45))

    # Many-to-Many relationship with Driver
    # drivers = db.relationship('Driver', secondary=bus_driver,
    #                                      backref=db.backref('buses_associated', lazy='dynamic'))

    def __repr__(self) -> str:
        return f"Department({self.id}, {self.name_dapartment})"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as a dictionary
        """
        return {
            "id": self.id,
            "name_dapartment": self.name_dapartment,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Department:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = Department(
            name_dapartment=dto_dict.get("name_dapartment"),
        )
        return obj
