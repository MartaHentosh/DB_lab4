from typing import List

from my_project.auth.dao.general_dao import GeneralDAO

from my_project.auth.domain.orders.company_asset import CompanyAsset


class CompanyAssetDAO(GeneralDAO):
    """
    Realisation of Client data access layer.
    """
    _domain_type = CompanyAsset
