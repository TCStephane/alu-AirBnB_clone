#!/usr/bin/python3
"""Unit tests for the BaseModel class."""
import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Test cases for BaseModel."""

    def test_id_is_unique_string(self):
        """Test that ids are strings and unique."""
        a, b = BaseModel(), BaseModel()
        self.assertIsInstance(a.id, str)
        self.assertNotEqual(a.id, b.id)

    def test_dates_are_datetime(self):
        """Test that created_at and updated_at are datetime objects."""
        a = BaseModel()
        self.assertIsInstance(a.created_at, datetime)
        self.assertIsInstance(a.updated_at, datetime)

    def test_str(self):
        """Test the string representation."""
        a = BaseModel()
        self.assertEqual(
            str(a), "[BaseModel] ({}) {}".format(a.id, a.__dict__))

    def test_save_updates_updated_at(self):
        """Test that save changes updated_at."""
        a = BaseModel()
        old = a.updated_at
        a.save()
        self.assertGreater(a.updated_at, old)

    def test_to_dict(self):
        """Test the dictionary representation."""
        a = BaseModel()
        a.name = "x"
        d = a.to_dict()
        self.assertEqual(d["__class__"], "BaseModel")
        self.assertEqual(d["name"], "x")
        self.assertEqual(d["created_at"], a.created_at.isoformat())
        self.assertEqual(d["updated_at"], a.updated_at.isoformat())
        self.assertIn("created_at", a.__dict__)
        self.assertIsInstance(a.created_at, datetime)

    def test_from_dict(self):
        """Test recreating an instance from a dictionary."""
        a = BaseModel()
        a.my_number = 89
        b = BaseModel(**a.to_dict())
        self.assertEqual(a.id, b.id)
        self.assertEqual(b.my_number, 89)
        self.assertEqual(a.created_at, b.created_at)
        self.assertIsInstance(b.created_at, datetime)
        self.assertFalse(hasattr(b, "__class__") and "__class__" in b.__dict__)
        self.assertIsNot(a, b)

    def test_args_ignored(self):
        """Test that positional arguments are ignored."""
        a = BaseModel("ignored", 1)
        self.assertNotIn("ignored", a.__dict__.values())


if __name__ == "__main__":
    unittest.main()
