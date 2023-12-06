from typing import List

from my_project.auth.dao.general_dao import GeneralDAO

from my_project.auth.domain.orders.assigment_date import AssigmentDate


class AssigmentDateDAO(GeneralDAO):
    """
    Realisation of Client data access layer.
    """
    _domain_type = AssigmentDate
