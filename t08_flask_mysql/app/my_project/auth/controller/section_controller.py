from t08_flask_mysql.app.my_project.auth.service import section_service
from t08_flask_mysql.app.my_project.auth.controller.general_controller import GeneralController


class SectionController(GeneralController):
    """
    Realisation of Section controller.
    """
    _service = section_service
