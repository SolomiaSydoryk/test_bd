from t08_flask_mysql.app.my_project.auth.service import supermarket_service
from t08_flask_mysql.app.my_project.auth.controller.general_controller import GeneralController


class SupermarketController(GeneralController):
    """
    Realisation of Supermarket controller.
    """
    _service = supermarket_service
