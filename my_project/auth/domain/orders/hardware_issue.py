from __future__ import annotations

from typing import Dict, Any

from my_project import db
from my_project.auth.domain.i_dto import IDto


class HardwareIssue(db.Model, IDto):
    """
    Model declaration for Data Mapper.
    """
    __tablename__ = "hardware_issue"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    decription: str = db.Column(db.String(100))
    request_date = db.Column(db.Date)

    company_hardware_id = db.Column(db.Integer, db.ForeignKey('company_hardware.id'), nullable=False)
    company_hardware = db.relationship('CompanyHardware', backref='company_hardware', lazy=True)

    location_id = db.Column(db.Integer, db.ForeignKey('location.id'), nullable=False)
    location = db.relationship('Location', backref='locations', lazy=True)

    def __repr__(self) -> str:
        return f"HardwareIssue({self.id}, {self.decription}, {self.request_date})"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as a dictionary
        """
        return {
            "id": self.id,
            "decription": self.decription,
            "request_date": self.request_date,
            "company_hardware": self.company_hardware.hardware_type if self.company_hardware_id is not None else "",
            "location": self.location.department if self.location_id is not None else "",
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> HardwareIssue:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = HardwareIssue(
            decription=dto_dict.get("decription"),
            request_date=dto_dict.get("request_date"),
            company_hardware_id=dto_dict.get("company_hardware_id"),
            location_id=dto_dict.get("location_id"),
        )
        return obj
