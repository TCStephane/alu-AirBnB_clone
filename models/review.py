#!/usr/bin/python3
"""Module defining the Review class."""
from models.base_model import BaseModel


class Review(BaseModel):
    """Represent a Review."""

    place_id = ""
    user_id = ""
    text = ""
