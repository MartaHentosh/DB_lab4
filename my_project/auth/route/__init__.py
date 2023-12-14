
from flask import Flask

from .error_handler import err_handler_bp


def register_routes(app: Flask) -> None:
    """
    Registers all necessary Blueprint routes
    :param app: Flask application object
    """
    app.register_blueprint(err_handler_bp)

    from .orders.department_route import department_bp
    from .orders.assigment_date_route import assigment_date_bp
    from .orders.company_hardware_route import company_hardware_bp
    from .orders.company_software_route import company_software_bp
    from .orders.employee_route import employee_bp
    from .orders.hardware_issue_route import hardware_issue_bp
    from .orders.location_route import location_bp
    from .orders.request_priority_route import request_priority_bp
    from .orders.request_route import request_bp
    from .orders.request_status_route import request_status_bp
    from .orders.request_type_route import request_type_bp
    from .orders.software_issue_route import software_issue_bp
    from .orders.company_asset_route import company_asset_bp

    app.register_blueprint(department_bp)
    app.register_blueprint(assigment_date_bp)
    app.register_blueprint(company_hardware_bp)
    app.register_blueprint(company_software_bp)
    app.register_blueprint(employee_bp)
    app.register_blueprint(hardware_issue_bp)
    app.register_blueprint(location_bp)
    app.register_blueprint(request_priority_bp)
    app.register_blueprint(request_bp)
    app.register_blueprint(request_status_bp)
    app.register_blueprint(request_type_bp)
    app.register_blueprint(software_issue_bp)
    app.register_blueprint(company_asset_bp)
