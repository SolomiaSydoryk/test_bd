from t08_flask_mysql.app.my_project.auth.dao.general_dao import GeneralDAO
from t08_flask_mysql.app.my_project.auth.domain import Section


class SectionDAO(GeneralDAO):
    """
    Realisation of Section data access layer.
    """
    _domain_type = Section
