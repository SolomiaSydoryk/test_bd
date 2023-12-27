from __future__ import annotations
from typing import Dict, Any

from t08_flask_mysql.app.my_project import db
from t08_flask_mysql.app.my_project.auth.domain.i_dto import IDto
from sqlalchemy import Index

interactive_advertising_panel_has_commercials = db.Table(
    'interactive_advertising_panel_has_commercials',
    db.Column('interactive_advertising_panel_id', db.Integer, db.ForeignKey('interactive_advertising_panel.id')),
    db.Column('commercials_id', db.Integer, db.ForeignKey('commercials.id')),
    db.UniqueConstraint('interactive_advertising_panel_id', 'commercials_id',
                        name='uq_interactive_advertising_panel_has_commercials'),
    extend_existing=True
)

supermarket_has_interactive_advertising_panel = db.Table(
    'supermarket_has_interactive_advertising_panel',
    db.Column('interactive_advertising_panel_id', db.Integer, db.ForeignKey('interactive_advertising_panel.id'),
              primary_key=True),
    db.Column('supermarket_id', db.Integer, db.ForeignKey('supermarket.id'), primary_key=True),
    db.Column('supermarket_address_id', db.Integer, db.ForeignKey('supermarket_address.id'), primary_key=True),
    db.Column('interactive_advertising_panel_specifications_id', db.Integer,
              db.ForeignKey('interactive_advertising_panel_specifications.id'), primary_key=True),
    db.Column('interactive_advertising_panel_section_id', db.Integer,
              db.ForeignKey('interactive_advertising_panel_section.id'), primary_key=True),
    db.UniqueConstraint('interactive_advertising_panel_id', 'commercials_id',
                        'interactive_advertising_panel_specifications_id', 'interactive_advertising_panel_section_id',
                        'supermarket_address_id',
                        name='uq_supermarket_has_interactive_advertising_panel'),
    extend_existing=True
)


class InteractiveAdvertisingPanel(db.Model, IDto):
    """
    Model declaration for InteractiveAdvertisingPanel.
    """
    __tablename__ = "interactive_advertising_panel"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    number = db.Column(db.String(20), nullable=False)
    specifications_id = db.Column(db.Integer, nullable=False, primary_key=True)
    section_id = db.Column(db.Integer, nullable=False, primary_key=True)

    # Relationship M:M with Commercials
    commercials = db.relationship("Commercials",
                                  secondary="interactive_advertising_panel_has_commercials",
                                  back_populates="interactive_advertising_panels")
    # Relationship M:M with Supermarket
    supermarkets = db.relationship("Supermarket",
                                   secondary="supermarket_has_interactive_advertising_panel",
                                   back_populates="interactive_advertising_panels")
    # Relationship M:1 with Specification
    specifications = db.relationship("Specification", backref="interactive_advertising_panels")
    # Relationship 1:M with Section
    sections = db.relationship("Section", backref="interactive_advertising_panels")

    __table_args__ = (
        Index('fk_interactive_advertising_panel_section1', 'fk_interactive_advertising_panel_specifications1'),
        {},
    )

    def __repr__(self) -> str:
        return (f"InteractiveAdvertisingPanel(id={self.id}, number={self.number}, section_id={self.section_id}, "
                f"specifications_id={self.specifications_id},)")

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as dictionary
        """
        return {
            "id": self.id,
            "number": self.number,
            "section_id": self.section_id,
            "specifications_id": self.specifications_id,

        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> InteractiveAdvertisingPanel:
        """
        Creates domain object from DTO        :param dto_dict:  object
        :return: Domain object
        """
        obj = InteractiveAdvertisingPanel(
            number=dto_dict.get("number"),
            section_id=dto_dict.get("section_id"),
            specifications_id=dto_dict.get("specifications_id"),
        )
        return obj
