from __future__ import annotations

from typing import Dict, Any

from my_project import db
from my_project.auth.domain.i_dto import IDto


class RequestStatus(db.Model, IDto):
    """
    Model declaration for Data Mapper.
    """
    __tablename__ = "request_status"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    request_status: str = db.Column(db.String(45))

    request_id = db.Column(db.Integer, db.ForeignKey('request.id'), nullable=False)
    request = db.relationship('Request', backref='request_statuses', lazy=True)
    # Many-to-Many relationship with Driver
    # drivers = db.relationship('Driver', secondary=bus_driver,
    #                                      backref=db.backref('buses_associated', lazy='dynamic'))

    def __repr__(self) -> str:
        return f"RequestStatus({self.id}, {self.request_status})"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as a dictionary
        """
        return {
            "id": self.id,
            "request_status": self.request_status,
            "request": self.request.id if self.request_id is not None else "",
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> RequestStatus:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = RequestStatus(
            request_status=dto_dict.get("request_status"),
            request_id=dto_dict.get("request_id"),
        )
        return obj
