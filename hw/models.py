from sqlalchemy import Column, Integer, String

from db import Base


class Contact(Base):
    __tablename__ = 'contacts'
    id = Column(Integer, primary_key=True)
    first_name = Column(String(120), nullable=False)
    last_name = Column(String(120), nullable=False)
    email = Column('email', String(100), nullable=True)
    cell_phone = Column('cell_phone', String(100), nullable=True)
    address = Column('address', String(100), nullable=True)