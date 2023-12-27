from t08_flask_mysql.app.my_project.auth.service.general_service import GeneralService
from t08_flask_mysql.app.my_project.auth.dao import commercials_dao


class CommercialsService(GeneralService):
    _dao = commercials_dao
