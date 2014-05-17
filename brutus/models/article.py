""" brutus/models/article - article model """

from sqlalchemy import (Column, ForeignKey,
                        Integer, String,
                        DateTime, Text)
from sqlalchemy.orm import relationship

from brutus.models import Base


class Article(Base):
    __tablename__ = "article"

    id = Column(Integer, primary_key=True)
    title = Column(String(250), nullable=False)
    body = Column(Text)
    created = Column(DateTime)
    modified = Column(DateTime)
    published = Column(DateTime)

    def __repr__(self):
        return "<Article(id={_id}, title={title})>".format(_id=self.id,
                                                           title=self.title)
