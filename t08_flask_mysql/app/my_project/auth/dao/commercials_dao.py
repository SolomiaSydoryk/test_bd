from sqlalchemy import joinedload

from t08_flask_mysql.app.my_project.auth.dao.general_dao import GeneralDAO
from t08_flask_mysql.app.my_project.auth.domain import Commercials
from t08_flask_mysql.app.my_project.auth.domain.interactive_advertising_panel import InteractiveAdvertisingPanel
from t08_flask_mysql.app.my_project.auth.domain.interactive_advertising_panel import \
    interactive_advertising_panel_has_commercials


class CommercialsDAO(GeneralDAO):
    """
    Realisation of Commercials data access layer.
    """
    _domain_type = Commercials

    def find_interactive_advertising_panels(self, commercial_id: int):
        """
        Find interactive advertising panel associated with a specific commercial.
        :param commercial_id: ID of the commercial
        :return: List of InteractiveAdvertisingPanel objects associated with the commercial
        """
        # Assuming that you have a session object, replace it with your actual SQLAlchemy session
        session = self.get_session()

        commercial = session.query(Commercials).filter_by(id=commercial_id).first()

        # Query the association table to get the interactive advertising panel IDs associated with the commercial
        interactive_advertising_panels_ids = (
            session.query(interactive_advertising_panel_has_commercials.c.interactive_advertising_panel_id)
            .filter(interactive_advertising_panel_has_commercials.c.commercial_id == commercial_id)
            .all()
        )

        # Extract solar panel IDs from the result
        interactive_advertising_panel_ids = [interactive_advertising_panel_id for (interactive_advertising_panel_id,) in
                                             interactive_advertising_panels_ids]

        # Query the SolarPanel table to get the SolarPanel objects associated with the solar panel IDs
        interactive_advertising_panels = session.query(InteractiveAdvertisingPanel).filter(
            InteractiveAdvertisingPanel.id.in_(interactive_advertising_panel_ids)).all()

        commercial_data = {
            "commercial": commercial.put_into_dto(),
            "interactive_advertising_panels": [interactive_advertising_panel.put_into_dto() for
                                               interactive_advertising_panel in interactive_advertising_panels]
        }

        return commercial_data

    def add_interactive_advertising_panel_to_commercial(self, commercial_id: int,
                                                        interactive_advertising_panel_id: int):
        session = self.get_session()

        association = interactive_advertising_panel_has_commercials.insert().values(
            commercial_id=commercial_id,
            interactive_advertising_panel_id=interactive_advertising_panel_id
        )

        session.execute(association)

        session.commit()

    def remove_interactive_advertising_panel_from_commercial(self, commercial_id: int,
                                                             interactive_advertising_panel_id: int):
        session = self.get_session()

        # Delete the association from the interactive_advertising_panel_has_commercials table
        session.execute(
            interactive_advertising_panel_has_commercials.delete()
            .where(interactive_advertising_panel_has_commercials.c.commercial_id == commercial_id)
            .where(
                interactive_advertising_panel_has_commercials.c.interactive_advertising_panel_id == interactive_advertising_panel_id)
        )

        session.commit()

    def find_by_id_with_interactive_advertising_panels(self, commercial_id: int):
        session = self.get_session()

        commercial = (
            session.query(Commercials)
            .options(joinedload(Commercials.interactive_advertising_panels))
            .filter(Commercials.id == commercial_id)
            .first()
        )

        return commercial
