from t08_flask_mysql.app.my_project.auth.service import commercials_service
from t08_flask_mysql.app.my_project.auth.controller.general_controller import GeneralController


class CommercialsController(GeneralController):
    """
    Realisation of Commercials controller.
    """
    _service = commercials_service


def find_interactive_advertising_panel(self, interactive_advertising_panel_id: int):
    return self._service.find_interactive_advertising_panel(interactive_advertising_panel_id)


def add_interactive_advertising_panel_to_commercials(self, interactive_advertising_panel_id: int, commercials_id: int):
    self._service.add_interactive_advertising_panel_to_commercials(interactive_advertising_panel_id, commercials_id)


def remove_interactive_advertising_panel_from_commercials(self, interactive_advertising_panel_id: int,
                                                          commercials_id: int):
    self._service.remove_interactive_advertising_panel_from_commercials(interactive_advertising_panel_id,
                                                                        commercials_id)


def find_by_id_with_interactive_advertising_panel(self, interactive_advertising_panel_id: int):
    return self._service.find_by_id_with_interactive_advertising_panel(interactive_advertising_panel_id)
