from typing import TYPE_CHECKING

from sqlalchemy import Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship

from app.db.base_class import Base


class Grid(Base):
    __table_args__ = {"schema": "forecast"}

    gridID = Column(String, primary_key=True, index=True)
    gridRow = Column(Integer, index=True)
    gridColumn = Column(Integer, index=True)
    latMin = Column(Float, index=True)
    lngMin = Column(Float, index=True)
    latMax = Column(Float, index=True)
    lngMax = Column(Float, index=True)
    P_CODE = Column(String, index=True)
    A_CODE = Column(String, index=True)
    T_CODE = Column(String, index=True)
    P_NAME_E = Column(Integer, index=True)
    A_NAME_E = Column(Integer, index=True)
    T_NAME_E = Column(Integer, index=True)

    # owner_id = Column(Integer, ForeignKey("user.id"))
