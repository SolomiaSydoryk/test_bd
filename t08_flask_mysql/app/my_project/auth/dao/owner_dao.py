from t08_flask_mysql.app.my_project.auth.dao.general_dao import GeneralDAO
from t08_flask_mysql.app.my_project.auth.domain import Owner


class OwnerDAO(GeneralDAO):
    """
    Realisation of Owner data access layer.
    """
    _domain_type = Owner
