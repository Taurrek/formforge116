from sqlalchemy import (
    Column, Integer, Numeric, String, Text, DateTime, func
)
from .db import Base

class DrillPack(Base):
    __tablename__ = 'drill_packs'
    id             = Column(Integer, primary_key=True)
    coach_id       = Column(Integer, nullable=False)
    title          = Column(String, nullable=False)
    description    = Column(Text)
    file_url       = Column(String, nullable=False)
    price_cents    = Column(Integer, nullable=False)
    commission_pct = Column(Numeric(5, 2), default=30.00)
    created_at     = Column(DateTime, server_default=func.now())
