""" brutus/models/org - org (organization) model

The org model is for Market Managers
"""

from sqlalchemy import (Column, ForeignKey,
                        Integer, String,
                        DateTime, Text)
from sqlalchemy.orm import relationship

from brutus.models import Base


class Org(Base):
    __tablename__ = "orgs"

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=True)
    description = Column(Text)
    hours = Column(Text)
    street = Column(String)
    city = Column(String)
    zipcode = Column(String)
    longitude = Column(Float)
    latitude = Column(Float)
    created = Column(DateTime)
    created = Column(DateTime)
    user = relationship('User')

    def __repr__(self):
        return "<Org(id={_id}, name={n})>".format(_id=self.id,
                                                  n=self.name)
