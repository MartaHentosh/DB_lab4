
# orders DB
from .orders.department_dao import DepartmentDAO
from .orders.assigment_date_dao import AssigmentDateDAO
from .orders.company_hardware_dao import CompanyHardwareDAO
from .orders.company_software_dao import CompanySoftwareDAO
from .orders.employee_dao import EmployeeDAO
from .orders.hardware_issue_dao import HardwareIssueDAO
from .orders.location_dao import LocationDAO
from .orders.request_dao import RequestDAO
from .orders.request_priority_dao import RequestPriorityDAO
from .orders.request_status_dao import RequestStatusDAO
from .orders.request_type_dao import RequestTypeDAO
from .orders.software_issue_dao import SoftwareIssueDAO

department_dao = DepartmentDAO()
assigment_date = AssigmentDateDAO()
company_hardware = CompanyHardwareDAO()
company_software = CompanySoftwareDAO()
employee = EmployeeDAO()
hardware_issue = HardwareIssueDAO()
location = LocationDAO()
request = RequestDAO()
request_priority = RequestPriorityDAO()
request_status = RequestStatusDAO()
request_type = RequestTypeDAO()
software_issue = SoftwareIssueDAO()