#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
import models
from os import getenv


from sqlalchemy import (
        Column,
        String,
        ForeignKey,
        Integer,
        Float,
        Table
        )

from sqlalchemy.orm import relationship

metadata = Base.metadata

association_table = Table(
        "place_amenity",
        metadata,
        Column(
            "place_id",
            String(60),
            ForeignKey("places.id"),
            primary_key=True,
            nullable=False
            ),
        Column(
            "amenity_id",
            String(60),
            ForeignKey("amenities.id"),
            primary_key=True,
            nullable=False
            ))


class Place(BaseModel, Base):

    """ A place to stay """
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float)
    longitude = Column(Float)

    reviews = relationship("Review", backref="place", cascade="delete")
    amenities = relationship(
            "Amenity",
            secondary=association_table,
            viewonly=False
            )
    amenity_ids = []

    if getenv("HBNB_TYPE_STORAGE", None) != "db":
        @property
        def reviews(self):
            """Getter method for reviews attribute for FileStorage"""
            from models.review import Review
            review_list = []
            for review in list(models.storage.all(Review).values()):
                if review.place_id == self.id:
                    review_list.append(review)
            return review

        @property
        def amenities(self):
            """Getter method for amenities attribute for FileStorage"""
            from models.amenity import Amenity
            amenity_list = []
            for amenity in list(models.storage.all(Amenity).values()):
                if amenity.id in self.amenity_ids:
                    amenity_list.append(amenity)
            return amenity_list

        @amenities.setter
        def amenities(self, value):
            """Setter method for amenities property for FileStorage"""
            from models.amenity import Amenity
            if type(value) == Amenity:
                self.amenity_ids.append(value.id)
