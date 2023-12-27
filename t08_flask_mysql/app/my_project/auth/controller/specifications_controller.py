from t08_flask_mysql.app.my_project.auth.service import specifications_service
from t08_flask_mysql.app.my_project.auth.controller.general_controller import GeneralController


class SpecificationController(GeneralController):
    """
    Realisation of Specification controller.
    """
    _service = specifications_service
