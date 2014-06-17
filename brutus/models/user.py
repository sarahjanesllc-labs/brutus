""" brutus/models/user - user model """

from sqlalchemy import (Column, ForeignKey, Boolean,
                        Integer, String,
                        DateTime, Text)
from sqlalchemy.orm import relationship, backref

from brutus.models import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False)
    password = Column(String, nullable=False)
    email = Column(String, nullable=False)
    created = Column(DateTime)
    vendor_id = Column(Integer, ForeignKey('vendor.id'))
    org_id = Column(Integer, ForeignKey('org.id'))

    def __repr__(self):
        return "<User(id={_id}, username={u}, " \
               "email={e})>".format(_id=self.id, u=self.username, e=self.email)
