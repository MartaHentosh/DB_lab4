from typing import List

from my_project.auth.dao.general_dao import GeneralDAO

from my_project.auth.domain.orders.location import Location


class LocationDAO(GeneralDAO):
    """
    Realisation of Client data access layer.
    """
    _domain_type = Location
