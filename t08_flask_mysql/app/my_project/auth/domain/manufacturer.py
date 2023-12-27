from __future__ import annotations
from typing import Dict, Any

from t08_flask_mysql.app.my_project import db
from t08_flask_mysql.app.my_project.auth.domain.i_dto import IDto
from sqlalchemy import UniqueConstraint

supermarket_has_manufacturer = db.Table(
    'supermarket_has_manufacturer',
    db.Column('supermarket_id', db.Integer, db.ForeignKey('supermarket.id'), primary_key=True),
    db.Column('supermarket_address_id', db.Integer, db.ForeignKey('supermarket_address.id'), primary_key=True),
    db.Column('manufacturer_id', db.Integer, db.ForeignKey('manufacturer.id'), primary_key=True),
    db.UniqueConstraint('supermarket_id', 'manufacturer_id', name='uq_supermarket_has_manufacturer'),
    extend_existing=True
)


class Manufacturer(db.Model, IDto):
    """
    Model declaration for Manufacturer.
    """
    __tablename__ = "manufacturer"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(45), nullable=False)
    phone = db.Column(db.String(13), nullable=False)
    site = db.Column(db.String(30), nullable=False)

    supermarkets = db.relationship("Supermarket", secondary="supermarket_has_manufacturer",
                                   back_populates="manufacturers")
    __table_args__ = (
        UniqueConstraint('phone', 'site', 'email'),
        {},
    )

    def __repr__(self) -> str:
        return (f"Manufacturer(id={self.id}, '{self.name}', '{self.email},' "
                f"'{self.phone}', '{self.site}'")

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as dictionary
        """
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "phone": self.phone,
            "site": self.site,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Manufacturer:
        """
        Creates domain object from DTO        :param dto_dict:  object
        :return: Domain object
        """
        obj = Manufacturer(
            name=dto_dict.get("name"),
            email=dto_dict.get("email"),
            phone=dto_dict.get("phone"),
            site=dto_dict.get("site"),
        )
        return obj
