from t08_flask_mysql.app.my_project.auth.dao.general_dao import GeneralDAO
from t08_flask_mysql.app.my_project.auth.domain import InteractiveAdvertisingPanel

from t08_flask_mysql.app.my_project.auth.domain.interactive_advertising_panel import \
    interactive_advertising_panel_has_commercials
from t08_flask_mysql.app.my_project.auth.domain.commercials import Commercials

from t08_flask_mysql.app.my_project.auth.domain.interactive_advertising_panel import \
    supermarket_has_interactive_advertising_panel
from t08_flask_mysql.app.my_project.auth.domain.supermarket import Supermarket

from sqlalchemy import joinedload


class InteractiveAdvertisingPanelDAO(GeneralDAO):
    """
    Realisation of InteractiveAdvertisingPanel data access layer.
    """
    _domain_type = InteractiveAdvertisingPanel

    def find_commercial(self, interactive_advertising_panel_id: int):
        """
        Find interactive advertising panel and its associated commercials.
        :param interactive_advertising_panel_id: ID of the interactive_advertising_panel
        :return: Dictionary containing information about the interactive advertising panel and its commercials
        """
        # Assuming that you have a session object, replace it with your actual SQLAlchemy session
        session = self.get_session()

        # Query the InteractiveAdvertisingPanel table to get the InteractiveAdvertisingPanel object
        interactive_advertising_panel = session.query(InteractiveAdvertisingPanel).filter_by(id=interactive_advertising_panel_id).first()

        # Query the association table to get the commercials IDs associated with the interactive advertising panel
        commercial_ids = (
            session.query(interactive_advertising_panel_has_commercials.c.commercials_id)
            .filter(interactive_advertising_panel_has_commercials.c.interactive_advertising_panel_id == interactive_advertising_panel_id)
            .all()
        )

        # Extract commercials IDs from the result
        commercial_ids = [commercials_id for (commercials_id,) in commercial_ids]

        # Query the Commercials table to get the Commercials objects associated with the commercials IDs
        commercials = session.query(Commercials).filter(Commercials.id.in_(commercial_ids)).all()

        # Create a dictionary to store information about the interactive advertising panel and its commercials
        interactive_advertising_panel_data = {
            "interactive_advertising_panel": interactive_advertising_panel.put_into_dto(),
            "commercials": [commercial.put_into_dto() for commercial in commercials]
        }

        return interactive_advertising_panel_data

    def interactive_advertising_panel_find_supermarket(self, interactive_advertising_panel_id: int):
        """
        Find interactive advertising panel associated with a specific supermarket.
        :param interactive_advertising_panel_id: ID of the supermarket
        :return: List of InteractiveAdvertisingPanel objects associated with the supermarket
        """
        # Assuming that you have a session object, replace it with your actual SQLAlchemy session
        session = self.get_session()

        # Query the association table to get the interactive advertising panel IDs associated with the supermarket
        supermarkets_ids = (
            session.query(supermarket_has_interactive_advertising_panel.c.supermarkets_id)
            .filter(supermarket_has_interactive_advertising_panel.c.interactive_advertising_panel_id == interactive_advertising_panel_id)
            .all()
        )

        # Extract supermarket IDs from the result
        supermarket_ids = [supermarket_id for (supermarket_id,) in supermarkets_ids]

        # Query the Supermarket table to get the Supermarket objects associated with the supermarket IDs
        supermarkets = session.query(Supermarket).filter(Supermarket.id.in_(supermarket_ids)).all()

        return [supermarket.put_into_dto() for supermarket in supermarkets]

    def find_all_supermarkets(self):
        """
        Find all supermarkets.
        :return: List of Supermarket objects
        """
        session = self.get_session()
        return session.query(Supermarket).all()

    def find_all_commercials(self):
        session = self.get_session()
        return session.query(Commercials).all()

    def add_commercial_to_interactive_advertising_panel(self, interactive_advertising_panel_id: int, commercial_id: int):
        session = self.get_session()

        association = interactive_advertising_panel_has_commercials.insert().values(
            interactive_advertising_panel_id=interactive_advertising_panel_id,
            commercial_id=commercial_id
        )

        session.execute(association)

        session.commit()

    def remove_commercial_from_interactive_advertising_panel(self, interactive_advertising_panel_id: int, commercial_id: int):
        """
        Removes a commercial from a specific interactive advertising panel in the database.
        :param interactive_advertising_panel_id: ID of the interactive advertising panel
        :param commercial_id: ID of the battery
        :return: None
        """
        session = self.get_session()

        # Delete the association from the interactive_advertising_panel_has_commercials table
        session.execute(
            interactive_advertising_panel_has_commercials.delete()
            .where(interactive_advertising_panel_has_commercials.c.interactive_advertising_panel_id == interactive_advertising_panel_id)
            .where(interactive_advertising_panel_has_commercials.c.commercial_id == commercial_id)
        )

        session.commit()

    def find_by_id_with_commercials(self, interactive_advertising_panel_id: int):
        """
        Finds an interactive advertising panel by ID with information about connected batteries.
        :param interactive_advertising_panel_id: ID of the interactive advertising panel
        :return: InteractiveAdvertisingPanel object with connected commercials
        """
        session = self.get_session()

        interactive_advertising_panel = (
            session.query(InteractiveAdvertisingPanel)
            .options(joinedload(InteractiveAdvertisingPanel.commercials))
            .filter(InteractiveAdvertisingPanel.id == interactive_advertising_panel_id)
            .first()
        )

        return interactive_advertising_panel
