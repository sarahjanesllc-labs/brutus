""" brutus/models/event - events model """

from sqlalchemy import (Column, ForeignKey,
                        Integer, String,
                        DateTime, Text)
from sqlalchemy.orm import relationship

from brutus.models import Base


class Event(Base):
    __tablename__ = "event"

    id = Column(Integer, primary_key=True)
    title = Column(String(250), nullable=True)
    body = Column(Text)
    created = Column(DateTime)
    startdate = Column(DateTime)
    stopdate = Column(DateTime)
    starttime = Column(DateTime)
    stoptime = Column(DateTime)

    def __repr__(self):
        return "<Event(id={_id}, title={t})>".format(_id=self.id,
                                                     t=self.title)
