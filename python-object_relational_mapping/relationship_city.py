#!/usr/bin/python3
"""Defines the City class, linked to the MySQL table cities."""
from relationship_state import Base
from sqlalchemy import Column, ForeignKey, Integer, String


class City(Base):
    """City class, linked to the MySQL table cities."""
    __tablename__ = "cities"

    id = Column(Integer, primary_key=True, autoincrement=True,
                nullable=False, unique=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
