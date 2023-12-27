from t08_flask_mysql.app.my_project.auth.dao.general_dao import GeneralDAO
from t08_flask_mysql.app.my_project.auth.domain import Specifications


class SpecificationsDAO(GeneralDAO):
    """
    Realisation of Specifications data access layer.
    """
    _domain_type = Specifications
