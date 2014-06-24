""" brutus/models/user - user model """

from sqlalchemy import (Column, ForeignKey, Boolean,
                        Integer, String,
                        DateTime, Float)
from sqlalchemy.orm import relationship, backref

from brutus.models import Base
from brutus.models.org import Org


class Category(Base):
    __tablename__ = "product_categories"

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    slug = Column(String(255), nullable=False)


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True)
    slug = Column(String(255), nullable=False)
    title = Column(String(255), nullable=False)
    price = Column(Float())
    unit = Column(String(255))
    created = Column(DateTime)
    expires = Column(DateTime)
    org_id = Column(Integer, ForeignKey('org.id'))
    category_id = Column(Integer, ForeignKey('category.id'))

    def __repr__(self):
        return "<Product(id={_id}, title={t})>".format(
            _id=self.id, t=self.title)

class ProductImage(Base):
    __tablename__ = "product_images"

    id = Column(Integer, primary_key=True)
    filename = Column(String(255), nullable=False)
    path = Column(String(255))
    product = relationship('Product')
