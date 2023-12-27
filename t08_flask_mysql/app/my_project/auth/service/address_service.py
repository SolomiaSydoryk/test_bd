from t08_flask_mysql.app.my_project.auth.service.general_service import GeneralService
from t08_flask_mysql.app.my_project.auth.dao import address_dao


class AddressService(GeneralService):
    _dao = address_dao
