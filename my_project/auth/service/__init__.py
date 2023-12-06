from .orders.department_service import DepartmentService
from .orders.assigment_date_service import AssigmentDateService
from .orders.company_hardware_service import CompanyHardwareService
from .orders.company_software_service import CompanySoftwareService
from .orders.employee_service import EmployeeService
from .orders.hardware_issue_service import HardwareIssueService
from .orders.location_service import LocationService
from .orders.request_service import RequestService
from .orders.request_priority_service import RequestPriorityService
from .orders.request_status_service import RequestStatusService
from .orders.request_type_service import RequestTypeService
from .orders.software_issue_service import SoftwareIssueService

department_service = DepartmentService()
assigment_date_service = AssigmentDateService()
company_hardware_service = CompanyHardwareService()
company_software_service = CompanySoftwareService()
employee_service = EmployeeService()
hardware_issue_service = HardwareIssueService()
location_service = LocationService()
request_service = RequestService()
request_priority_service = RequestPriorityService()
request_status_service = RequestStatusService()
request_type_service = RequestTypeService()
software_issue_service = SoftwareIssueService()
