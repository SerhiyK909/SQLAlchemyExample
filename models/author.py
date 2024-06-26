from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from models.base import Base


# Define the User model
class Author(Base):
    __tablename__ = 'authors'
    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String)
    last_name = Column(String)
    books = relationship("Book", back_populates="author")