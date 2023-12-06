from my_project.auth.controller.general_controller import GeneralController
from my_project.auth.service import location_service


class LocationController(GeneralController):
    """
    Realisation of Client controller.
    """
    _service = location_service
