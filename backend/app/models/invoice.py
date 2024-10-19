from sqlalchemy import Column, Integer, String, Float
from app.database import Base


class Invoice(Base):
    __tablename__ = "invoices"
    id = Column(Integer, primary_key=True, index=True)
    amount = Column(Float)
    description = Column(String)
