from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response

from t08_flask_mysql.app.my_project.auth.controller import interactive_advertising_panel_controller
from t08_flask_mysql.app.my_project.auth.domain import InteractiveAdvertisingPanel

interactive_advertising_panel_bp = Blueprint('interactive_advertising_panel', __name__,
                                             url_prefix='/interactive_advertising_panel')


@interactive_advertising_panel_bp.get('')
def get_all_interactive_advertising_panel() -> Response:
    return make_response(jsonify(interactive_advertising_panel_controller.find_all()), HTTPStatus.OK)


@interactive_advertising_panel_bp.get('/<int:interactive_advertising_panel_id>')
def get_interactive_advertising_panel(interactive_advertising_panel_id: int) -> Response:
    return make_response(jsonify(interactive_advertising_panel_controller.find_by_id(interactive_advertising_panel_id)),
                         HTTPStatus.OK)


@interactive_advertising_panel_bp.post('')
def create_interactive_advertising_panel() -> Response:
    content = request.get_json()
    obj = InteractiveAdvertisingPanel.create_from_dto(content)
    interactive_advertising_panel_controller.create(obj)
    return make_response(jsonify(obj.put_into_dto()), HTTPStatus.CREATED)


@interactive_advertising_panel_bp.put('/<int:interactive_advertising_panel_id>')
def update_interactive_advertising_panel(interactive_advertising_panel_id: int) -> Response:
    content = request.get_json()
    obj = InteractiveAdvertisingPanel.create_from_dto(content)
    interactive_advertising_panel_controller.update(interactive_advertising_panel_id, obj)
    return make_response("Interactive advertising panel updated", HTTPStatus.OK)


@interactive_advertising_panel_bp.patch('/<int:interactive_advertising_panel_id>')
def patch_interactive_advertising_panel(interactive_advertising_panel_id: int) -> Response:
    content = request.get_json()
    interactive_advertising_panel_controller.patch(interactive_advertising_panel_id, content)
    return make_response("Interactive advertising panel updated", HTTPStatus.OK)


@interactive_advertising_panel_bp.delete('/<int:interactive_advertising_panel_id>')
def delete_interactive_advertising_panel(interactive_advertising_panel_id: int) -> Response:
    interactive_advertising_panel_controller.delete(interactive_advertising_panel_id)
    return make_response("Interactive advertising panel deleted", HTTPStatus.OK)
