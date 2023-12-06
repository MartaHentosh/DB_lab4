from __future__ import annotations

from typing import Dict, Any

from my_project import db
from my_project.auth.domain.i_dto import IDto


class SoftwareIssue(db.Model, IDto):
    """
    Model declaration for Data Mapper.
    """
    __tablename__ = "software_issue"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    description_issue: str = db.Column(db.String(100))

    company_software_id = db.Column(db.Integer, db.ForeignKey('company_software.id'), nullable=False)
    company_software = db.relationship('CompanySoftware', backref='company_software', lazy=True)

    location_id = db.Column(db.Integer, db.ForeignKey('location.id'), nullable=False)
    location = db.relationship('Location', backref='location', lazy=True)

    # Many-to-Many relationship with Driver
    # drivers = db.relationship('Driver', secondary=bus_driver,
    #                                      backref=db.backref('buses_associated', lazy='dynamic'))

    def __repr__(self) -> str:
        return f"SoftwareIssue({self.id})"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as a dictionary
        """
        return {
            "id": self.id,
            "description_issue": self.description_issue,
            "company_software": self.company_software.software_type if self.company_software_id is not None else "",
            "location": self.location.department if self.location_id is not None else "",
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> SoftwareIssue:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = SoftwareIssue(
            description_issue=dto_dict.get("description_issue"),
            company_software_id=dto_dict.get("company_software_id"),
            location_id=dto_dict.get("location_id"),
        )
        return obj
