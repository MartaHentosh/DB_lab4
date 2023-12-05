from __future__ import annotations

from typing import Dict, Any

from my_project import db
from my_project.auth.domain.i_dto import IDto


class Location(db.Model, IDto):
    """
    Model declaration for Data Mapper.
    """
    __tablename__ = "location"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    department: str = db.Column(db.String(45))
    room: str = db.Column(db.String(45))

    # Many-to-Many relationship with Driver
    # drivers = db.relationship('Driver', secondary=bus_driver,
    #                                      backref=db.backref('buses_associated', lazy='dynamic'))

    def __repr__(self) -> str:
        return f"Location({self.id}, {self.department}, {self.room})"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as a dictionary
        """
        return {
            "id": self.id,
            "department": self.department,
            "room": self.room,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Location:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = Location(
            department=dto_dict.get("department"),
            room=dto_dict.get("room"),
        )
        return obj
