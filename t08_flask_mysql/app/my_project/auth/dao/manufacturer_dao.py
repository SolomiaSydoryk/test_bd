from t08_flask_mysql.app.my_project.auth.dao.general_dao import GeneralDAO
from t08_flask_mysql.app.my_project.auth.domain import Manufacturer


class ManufacturerDAO(GeneralDAO):
    """
    Realisation of Manufacturer data access layer.
    """
    _domain_type = Manufacturer
