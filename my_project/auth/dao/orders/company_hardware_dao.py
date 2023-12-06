from typing import List

from my_project.auth.dao.general_dao import GeneralDAO

from my_project.auth.domain.orders.department import CompanyHardware


class CompanyHardwareDAO(GeneralDAO):
    """
    Realisation of Client data access layer.
    """
    _domain_type = CompanyHardware
