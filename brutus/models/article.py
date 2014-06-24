""" brutus/models/article - article model """

from sqlalchemy import (Column, ForeignKey,
                        Integer, String,
                        DateTime, Text)
from sqlalchemy.orm import relationship

from brutus.models import Base
from brutus.models.org import Org


class Article(Base):
    __tablename__ = "articles"

    id = Column(Integer, primary_key=True)
    title = Column(String(250), nullable=False)
    body = Column(Text)
    created = Column(DateTime)
    modified = Column(DateTime)
    published = Column(DateTime)
    expires = Column(DateTime)
    vendor_id = Column(Integer, ForeignKey('org.id'))

    def __repr__(self):
        return "<Article(id={_id}, title={title})>".format(_id=self.id,
                                                           title=self.title)
