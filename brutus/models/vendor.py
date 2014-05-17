""" brutus/models/vendor - vendor model """

from sqlalchemy import (Column, Sequence, ForeignKey, Boolean,
                        Integer, String, Float, DateTime, Text)
from sqlalchemy.orm import relationship

from brutus.models import Base


class Vendor(Base):
    __tablename__ = "vendors"

    id = Column(Integer, Sequence('vendor_id_seq'), primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String, nullable=False)
    street = Column(String)
    city = Column(String)
    zipcode = Column(String)
    longitude = Column(Float)
    latitude = Column(Float)
    created = Column(DateTime)

    def __repr__(self):
        return "<Vendor(id={_id}, " \
            "long={longitude}, " \
            "lat={latitude})>".format(_id=self.id,
                                      longitude=self.longitude,
                                      latitude=self.latitude)
