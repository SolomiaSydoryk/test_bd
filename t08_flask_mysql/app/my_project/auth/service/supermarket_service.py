from t08_flask_mysql.app.my_project.auth.service.general_service import GeneralService
from t08_flask_mysql.app.my_project.auth.dao import supermarket_dao


class SupermarketService(GeneralService):
    _dao = supermarket_dao
