from __future__ import annotations

from typing import Dict, Any

from my_project import db
from my_project.auth.domain.i_dto import IDto


class CompanySoftware(db.Model, IDto):
    """
    Model declaration for Data Mapper.
    """
    __tablename__ = "company_software"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    software_type: str = db.Column(db.String(45))
    software_version: str = db.Column(db.String(45))

    # Many-to-Many relationship with Driver
    # drivers = db.relationship('Driver', secondary=bus_driver,
    #                                      backref=db.backref('buses_associated', lazy='dynamic'))

    def __repr__(self) -> str:
        return f"CompanySoftware({self.id}, {self.software_type}, {self.software_version})"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as a dictionary
        """
        return {
            "id": self.id,
            "software_type": self.software_type,
            "software_version": self.software_version
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> CompanySoftware:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = CompanySoftware(
            software_type=dto_dict.get("software_type"),
            software_version=dto_dict.get("software_version"),
        )
        return obj
