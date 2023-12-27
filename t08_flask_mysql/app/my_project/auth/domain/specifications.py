from __future__ import annotations
from typing import Dict, Any

from t08_flask_mysql.app.my_project import db
from t08_flask_mysql.app.my_project.auth.domain.i_dto import IDto


class Specifications(db.Model, IDto):
    """
    Model declaration for Specifications.
    """
    __tablename__ = "specifications"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    model_year = db.Column(db.Integer, nullable=True)
    screen_resolution_capacity = db.Column(db.String(25), nullable=True)
    display_type = db.Column(db.String(15), nullable=True)
    HDR_support = db.Column(db.Boolean, nullable=True)
    video_signal_support = db.Column(db.Boolean, nullable=True)
    speaker_type = db.Column(db.String(45), nullable=True)
    auto_off_timer = db.Column(db.Boolean, nullable=True)
    operating_system = db.Column(db.String(25), nullable=True)
    level_of_energy_consumption = db.Column(db.String(5), nullable=True)
    frame_color = db.Column(db.String(25), nullable=True)
    TV_system = db.Column(db.String(25), nullable=True)
    weight = db.Column(db.Float, nullable=True)
    USB_ports = db.Column(db.String(25), nullable=True)
    WIFI_standart = db.Column(db.String(45), nullable=True)
    sound_processing = db.Column(db.String(30), nullable=True)
    refresh_rate = db.Column(db.String(10), nullable=True)
    screen_diagonal = db.Column(db.Integer, nullable=True)
    producer = db.Column(db.String(30), nullable=False)
    model = db.Column(db.String(50), nullable=True)

    interactive_advertising_panel = db.relationship("InteractiveAdvertisingPanel", backref="specifications")

    def __repr__(self) -> str:
        return (f"Specifications(id={self.id}, model_year={self.model_year}, "
                f"screen_resolution_capacity={self.screen_resolution_capacity}, display_type={self.display_type}, "
                f"HDR_support={self.HDR_support}, video_signal_support={self.video_signal_support}, "
                f"speaker_type={self.speaker_type}, auto_off_timer={self.auto_off_timer}, "
                f"operating_system={self.operating_system}, "
                f"level_of_energy_consumption={self.level_of_energy_consumption}, frame_color={self.frame_color}, "
                f"TV_system={self.TV_system}, weight={self.weight}, USB_ports={self.USB_ports}, "
                f"WIFI_standart={self.WIFI_standart}, sound_processing={self.sound_processing}, "
                f"refresh_rate={self.refresh_rate}, screen_diagonal={self.screen_diagonal}, producer={self.producer}, "
                f"model={self.model})")

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as dictionary
        """
        return {
            "id": self.id,
            "model_year": self.model_year,
            "screen_resolution_capacity": self.screen_resolution_capacity,
            "display_type": self.display_type,
            "HDR_support": self.HDR_support,
            "video_signal_support": self.video_signal_support,
            "speaker_type": self.speaker_type,
            "auto_off_timer": self.auto_off_timer,
            "operating_system": self.operating_system,
            "level_of_energy_consumption": self.level_of_energy_consumption,
            "frame_color": self.frame_color,
            "TV_system": self.TV_system,
            "weight": self.weight,
            "USB_ports": self.USB_ports,
            "WIFI_standart": self.WIFI_standart,
            "sound_processing": self.sound_processing,
            "refresh_rate": self.refresh_rate,
            "screen_diagonal": self.screen_diagonal,
            "producer": self.producer,
            "model": self.model,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Specifications:
        """
        Creates domain object from DTO        :param dto_dict:  object
        :return: Domain object
        """
        obj = Specifications(
            model_year=dto_dict.get("model_year"),
            screen_resolution_capacity=dto_dict.get("screen_resolution_capacity"),
            display_type=dto_dict.get("display_type"),
            HDR_support=dto_dict.get("HDR_support"),
            video_signal_support=dto_dict.get("video_signal_support"),
            speaker_type=dto_dict.get("speaker_type"),
            auto_off_timer=dto_dict.get("auto_off_timer"),
            operating_system=dto_dict.get("operating_system"),
            level_of_energy_consumption=dto_dict.get("level_of_energy_consumption"),
            frame_color=dto_dict.get("frame_color"),
            TV_system=dto_dict.get("TV_system"),
            weight=dto_dict.get("weight"),
            USB_ports=dto_dict.get("USB_ports"),
            WIFI_standart=dto_dict.get("WIFI_standart"),
            sound_processing=dto_dict.get("sound_processing"),
            refresh_rate=dto_dict.get("refresh_rate"),
            screen_diagonal=dto_dict.get("screen_diagonal"),
            producer=dto_dict.get("producer"),
            model=dto_dict.get("model"),
        )
        return obj
