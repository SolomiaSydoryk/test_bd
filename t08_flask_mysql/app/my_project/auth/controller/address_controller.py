from t08_flask_mysql.app.my_project.auth.service import address_service
from t08_flask_mysql.app.my_project.auth.controller.general_controller import GeneralController


class AddressController(GeneralController):
    """
    Realisation of Address controller.
    """
    _service = address_service
