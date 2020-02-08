from sqlalchemy import Integer, Column, create_engine, Numeric, Boolean, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

engine = create_engine('mysql://steven:password@127.0.0.1/sqlalchemy')


class Product(Base):
    __tablename__ = 'products'
    id=Column(Integer, primary_key=True)
    title=Column('title', String(32))
    in_stock=Column('in_stock', Boolean)
    quantity=Column('quantity', Integer)
    price=Column('price', Numeric)


class Article(Base):
    __tablename__ = 'articles'
    id = Column(Integer, primary_key=True)
    comments = relationship("Comment")


class Comment(Base):
    __tablename__ = 'comments'
    id = Column(Integer, primary_key=True)
    article_id = Column(Integer, ForeignKey('articles.id'))


'''
One to many, from the perspective of an individual object. Form the objects perspective
its one to many; it has money objects to its one. Many to one, say tires to a car,
is the other way. Again, from the point of view of the starting object we see that there
is some other object out there that takes several instance of our starting object.

One to many:
on the one object, we establish some primary key, fields, and a certain field that establishes
a relationship.

class Aricle:
    comments = relationship('Comment')
    
where Comment is some comment table.


Many to one:

Class Tire(Base):
    car_id = Column(Integer, ForiegnKey('cars.id'))
    car = realtionship('Car')


class Car(Base):
    id = Column(Integer, primary_key=True)
    
so whats happening in many to one is we're establishing a relationship in the many 
class AND  a foreign key.


Basically a relationship field is always declared on the object from whose perspective
the relationship is happening, and then the foreign key is establish on the object of whom
there are many. The point being that the foreign key field is what actually differentiates the 
two.




one to one


'''