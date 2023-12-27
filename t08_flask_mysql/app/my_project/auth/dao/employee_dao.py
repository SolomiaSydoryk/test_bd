from t08_flask_mysql.app.my_project.auth.dao.general_dao import GeneralDAO
from t08_flask_mysql.app.my_project.auth.domain import Employee


class EmployeeDAO(GeneralDAO):
    """
    Realisation of Employee data access layer.
    """
    _domain_type = Employee
