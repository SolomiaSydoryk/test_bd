from t08_flask_mysql.app.my_project.auth.dao.general_dao import GeneralDAO
from t08_flask_mysql.app.my_project.auth.domain import Address


class AddressDAO(GeneralDAO):
    """
    Realisation of Address data access layer.
    """
    _domain_type = Address
