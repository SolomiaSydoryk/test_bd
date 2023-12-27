from t08_flask_mysql.app.my_project.auth.dao.general_dao import GeneralDAO
from t08_flask_mysql.app.my_project.auth.domain import Supermarket
from t08_flask_mysql.app.my_project.auth.domain.interactive_advertising_panel import \
    supermarket_has_interactive_advertising_panel
from t08_flask_mysql.app.my_project.auth.domain.interactive_advertising_panel import InteractiveAdvertisingPanel


class SupermarketDAO(GeneralDAO):
    """
    Realisation of Supermarket data access layer.
    """
    _domain_type = Supermarket

    def supermarket_find_interactive_advertising_panel(self, supermarket_id: int):
        """
        Find supermarket associated with a specific interactive advertising panel.
        :param supermarket_id: ID of the interactive advertising panel
        :return: List of Supermarket objects associated with the interactive advertising panel
        """

        # Assuming that you have a session object, replace it with your actual SQLAlchemy session
        session = self.get_session()

        # Query the association table to get the supermarket IDs associated with the interactive advertising panel
        interactive_advertising_panels_ids = (
            session.query(supermarket_has_interactive_advertising_panel.c.interactive_advertising_panel_id)
            .filter(supermarket_has_interactive_advertising_panel.c.supermarket_id == supermarket_id)
            .all()
        )

        # Extract interactive advertising panel IDs from the result
        interactive_advertising_panel_ids = [supermarket_id for (supermarket_id,) in interactive_advertising_panels_ids]

        # Query the InteractiveAdvertisingPanel table to get the InteractiveAdvertisingPanel objects associated
        # with the interactive_advertising_panel IDs
        interactive_advertising_panels = session.query(InteractiveAdvertisingPanel).filter(
            InteractiveAdvertisingPanel.id.in_(interactive_advertising_panel_ids)).all()
        return [interactive_advertising_panel.put_into_dto() for interactive_advertising_panel in
                interactive_advertising_panels]
