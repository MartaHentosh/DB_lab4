from __future__ import annotations

from typing import Dict, Any

from my_project import db
from my_project.auth.domain.i_dto import IDto


class CompanyAsset(db.Model, IDto):
    """
    Model declaration for Data Mapper.
    """
    __tablename__ = "company_asset"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    asset_name: str = db.Column(db.String(100))
    asset_type: str = db.Column(db.String(45))

    employee_id = db.Column(db.Integer, db.ForeignKey('employee.id'), nullable=False)
    employee = db.relationship('Employee', backref='employees', lazy=True)

    def __repr__(self) -> str:
        return f"CompanyAsset({self.id}, {self.asset_name}, {self.asset_type})"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as a dictionary
        """
        return {
            "id": self.id,
            "asset_name": self.asset_name,
            "asset_type": self.asset_type,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> CompanyAsset:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = CompanyAsset(
            asset_name=dto_dict.get("asset_name"),
            asset_type=dto_dict.get("asset_type"),
        )
        return obj
