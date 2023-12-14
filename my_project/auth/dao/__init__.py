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
from .orders.company_asset_dao import CompanyAssetDAO

department_dao = DepartmentDAO()
assigment_date_dao = AssigmentDateDAO()
company_hardware_dao = CompanyHardwareDAO()
company_software_dao = CompanySoftwareDAO()
employee_dao = EmployeeDAO()
hardware_issue_dao = HardwareIssueDAO()
location_dao = LocationDAO()
request_dao = RequestDAO()
request_priority_dao = RequestPriorityDAO()
request_status_dao = RequestStatusDAO()
request_type_dao = RequestTypeDAO()
software_issue_dao = SoftwareIssueDAO()
company_asset_dao = CompanyAssetDAO()
