from t08_flask_mysql.app.my_project.auth.service.general_service import GeneralService
from t08_flask_mysql.app.my_project.auth.dao import owner_dao


class OwnerService(GeneralService):
    _dao = owner_dao
