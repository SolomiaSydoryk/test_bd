from t08_flask_mysql.app.my_project.auth.service.general_service import GeneralService
from t08_flask_mysql.app.my_project.auth.dao import specifications_dao


class SpecificationService(GeneralService):
    _dao = specifications_dao
