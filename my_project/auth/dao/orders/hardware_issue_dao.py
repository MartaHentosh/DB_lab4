from typing import List

from my_project.auth.dao.general_dao import GeneralDAO

from my_project.auth.domain.orders.hardware_issue import HardwareIssue


class HardwareIssueDAO(GeneralDAO):
    """
    Realisation of Client data access layer.
    """
    _domain_type = HardwareIssue
