""" brutus/models/org - org (organization) model

The org model is for Market Managers
"""

from sqlalchemy import (Column, ForeignKey,
                        Integer, String,
                        DateTime, Text)
from sqlalchemy.orm import relationship

from brutus.models import Base


class Org(Base):
    __tablename__ = "org"

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=True)
    created = Column(DateTime)

    def __repr__(self):
        return "<Org(id={_id}, name={n})>".format(_id=self.id,
                                                  n=self.name)
