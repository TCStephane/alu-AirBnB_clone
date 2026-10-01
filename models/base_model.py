#!/usr/bin/python3
"""Module defining the BaseModel class for all AirBnB clone models."""
import uuid
from datetime import datetime
import models


class BaseModel:
    """Base class defining common attributes and methods for all models."""

    def __init__(self, *args, **kwargs):
        """Initialize a new instance, or rebuild one from a dictionary."""
        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                if key in ("created_at", "updated_at"):
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)

    def __str__(self):
        """Return the string representation of the instance."""
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Update updated_at with the current time and save to storage."""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Return a dictionary of all keys and values of the instance."""
        result = dict(self.__dict__)
        result["__class__"] = self.__class__.__name__
        result["created_at"] = self.created_at.isoformat()
        result["updated_at"] = self.updated_at.isoformat()
        return result
