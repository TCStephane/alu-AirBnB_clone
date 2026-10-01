#!/usr/bin/python3
"""Module defining the City class."""
from models.base_model import BaseModel


class City(BaseModel):
    """Represent a City."""

    state_id = ""
    name = ""
