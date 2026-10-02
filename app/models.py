from sqlalchemy import Column, Integer, String, Float, ForeignKey
from app.database import Base

# Users table
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    role = Column(String, default="user")  # "admin" or "user"


# Inventory Items table
class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    quantity = Column(Integer, default=0)
    price = Column(Float)
    user_id = Column(Integer, ForeignKey("users.id"))  # Links item to the user who created it