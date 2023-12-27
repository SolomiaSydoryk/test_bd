from t08_flask_mysql.app.my_project.auth.service.general_service import GeneralService
from t08_flask_mysql.app.my_project.auth.dao import employee_dao


class EmployeeService(GeneralService):
    _dao = employee_dao
