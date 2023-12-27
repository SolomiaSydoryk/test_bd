from t08_flask_mysql.app.my_project.auth.service import manufacturer_service
from t08_flask_mysql.app.my_project.auth.controller.general_controller import GeneralController


class ManufacturerController(GeneralController):
    """
    Realisation of Manufacturer controller.
    """
    _service = manufacturer_service
