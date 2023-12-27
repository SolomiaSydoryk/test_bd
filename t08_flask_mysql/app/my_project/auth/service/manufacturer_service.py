from t08_flask_mysql.app.my_project.auth.service.general_service import GeneralService
from t08_flask_mysql.app.my_project.auth.dao import manufacturer_dao


class ManufacturerService(GeneralService):
    _dao = manufacturer_dao
