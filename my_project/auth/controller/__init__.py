from .orders.department_controller import DepartmentController
from .orders.assigment_date_controller import AssigmentDateController
from .orders.company_hardware_controller import CompanyHardwareController
from .orders.company_software_controller import CompanySoftwareController
from .orders.employee_controller import EmployeeController
from .orders.hardware_issue_controller import HardwareIssueController
from .orders.location_controller import LocationController
from .orders.request_controller import RequestController
from .orders.request_priority_controller import RequestPriorityController
from .orders.request_status_controller import RequestStatusController
from .orders.request_type_controller import RequestTypeController
from .orders.software_issue_controller import SoftwareIssueController
from .orders.company_asset_controller import CompanyAssetController

department_controller = DepartmentController()
assigment_date_controller = AssigmentDateController()
company_hardware_controller = CompanyHardwareController()
company_software_controller = CompanySoftwareController()
employee_controller = EmployeeController()
hardware_issue_controller = HardwareIssueController()
location_controller = LocationController()
request_controller = RequestController()
request_priority_controller = RequestPriorityController()
request_status_controller = RequestStatusController()
request_type_controller = RequestTypeController()
software_issue_controller = SoftwareIssueController()
company_asset_controller = CompanyAssetController()
