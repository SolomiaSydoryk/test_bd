from t08_flask_mysql.app.my_project.auth.service.general_service import GeneralService
from t08_flask_mysql.app.my_project.auth.dao import section_dao


class SectionService(GeneralService):
    _dao = section_dao
