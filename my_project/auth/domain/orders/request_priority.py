from __future__ import annotations

from typing import Dict, Any

from my_project import db
from my_project.auth.domain.i_dto import IDto


class RequestPriority(db.Model, IDto):
    """
    Model declaration for Data Mapper.
    """
    __tablename__ = "request_priority"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    priority: int = db.Column(db.Integer)

    request_id = db.Column(db.Integer, db.ForeignKey('request.id'), nullable=False)
    request = db.relationship('Request', backref='requests', lazy=True)

    # Many-to-Many relationship with Driver
    # drivers = db.relationship('Driver', secondary=bus_driver,
    #                                      backref=db.backref('buses_associated', lazy='dynamic'))

    def __repr__(self) -> str:
        return f"RequestPriority({self.id}, {self.priority})"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as a dictionary
        """
        return {
            "id": self.id,
            "priority": self.priority,
            "request": self.request.id if self.request_id is not None else "",
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> RequestPriority:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = RequestPriority(
            priority=dto_dict.get("priority"),
            request_id=dto_dict.get("request_id"),
        )
        return obj
