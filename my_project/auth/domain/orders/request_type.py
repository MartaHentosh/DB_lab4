from __future__ import annotations

from typing import Dict, Any

from my_project import db
from my_project.auth.domain.i_dto import IDto


class RequestType(db.Model, IDto):
    """
    Model declaration for Data Mapper.
    """
    __tablename__ = "request_type"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    request_id = db.Column(db.Integer, db.ForeignKey('request.id'), nullable=False)
    request = db.relationship('Request', backref='request_types', lazy=True)

    hardware_issue_id = db.Column(db.Integer, db.ForeignKey('hardware_issue.id'), nullable=False)
    hardware_issue = db.relationship('HardwareIssue', backref='hardware_issue', lazy=True)

    software_issue_id = db.Column(db.Integer, db.ForeignKey('software_issue.id'), nullable=False)
    software_issue = db.relationship('SoftwareIssue', backref='software_issue', lazy=True)
    # Many-to-Many relationship with Driver
    # drivers = db.relationship('Driver', secondary=bus_driver,
    #                                      backref=db.backref('buses_associated', lazy='dynamic'))

    def __repr__(self) -> str:
        return f"RequestType({self.id})"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as a dictionary
        """
        return {
            "id": self.id,
            "request": self.request_id,
            "hardware_issue_description": f"{self.hardware_issue.decription}" if self.hardware_issue_id is not None else "",
            "software_issue_description": f"{self.software_issue.description_issue}" if self.software_issue_id is not None else "",
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> RequestType:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = RequestType(
            request_id=dto_dict.get("request_id"),
            hardware_issue_id=dto_dict.get("hardware_issue_id"),
            software_issue_id=dto_dict.get("software_issue_id"),
        )
        return obj
