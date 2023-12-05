from __future__ import annotations

from typing import Dict, Any

from my_project import db
from my_project.auth.domain.i_dto import IDto


class CompanyHardware(db.Model, IDto):
    """
    Model declaration for Data Mapper.
    """
    __tablename__ = "company_hardware"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    hardware_type: str = db.Column(db.String(45))

    # Many-to-Many relationship with Driver
    # drivers = db.relationship('Driver', secondary=bus_driver,
    #                                      backref=db.backref('buses_associated', lazy='dynamic'))

    def __repr__(self) -> str:
        return f"CompanyHardware({self.id}, {self.hardware_type})"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as a dictionary
        """
        return {
            "id": self.id,
            "hardware_type": self.hardware_type,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> CompanyHardware:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = CompanyHardware(
            hardware_type=dto_dict.get("hardware_type"),
        )
        return obj
