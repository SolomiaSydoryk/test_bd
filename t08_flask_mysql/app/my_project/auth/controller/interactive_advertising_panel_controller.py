from t08_flask_mysql.app.my_project.auth.service import interactive_advertising_panel_service
from t08_flask_mysql.app.my_project.auth.controller.general_controller import GeneralController


class InteractiveAdvertisingPanelController(GeneralController):
    """
    Realisation of Interactive advertising panel controller.
    """
    _service = interactive_advertising_panel_service


def get_specifications_for_interactive_advertising_panel(self, interactive_advertising_panel_id: int):
    return self._service.get_specifications_for_interactive_advertising_panel(interactive_advertising_panel_id)


def get_section_for_interactive_advertising_panel(self, interactive_advertising_panel_id: int):
    return self._service.get_section_for_interactive_advertising_panel(interactive_advertising_panel_id)


def get_number_for_interactive_advertising_panel(self, interactive_advertising_panel_id: int):
    return self._service.get_number_for_interactive_advertising_panel(interactive_advertising_panel_id)


def find_commercials(self, commercials_id: int):
    return self._service.find_commercials(commercials_id)


def add_commercials_to_interactive_advertising_panel(self, commercials_id: int, interactive_advertising_panel_id: int):
    self._service.add_commercials_to_interactive_advertising_panel(commercials_id, interactive_advertising_panel_id)


def remove_commercials_from_interactive_advertising_panel(self, commercials_id: int, interactive_advertising_panel_id: int):
    self._service.remove_commercials_from_interactive_advertising_panel(commercials_id, interactive_advertising_panel_id)


def find_by_id_with_commercials(self, commercials_id: int):
    return self._service.find_by_id_with_commercials(commercials_id)
