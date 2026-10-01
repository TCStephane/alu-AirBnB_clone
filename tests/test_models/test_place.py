#!/usr/bin/python3
"""Unit tests for the Place class."""
import unittest
from models.base_model import BaseModel
from models.place import Place


class TestPlace(unittest.TestCase):
    """Test cases for Place."""

    def test_inheritance(self):
        """Test that Place inherits from BaseModel."""
        self.assertIsInstance(Place(), BaseModel)

    def test_attributes(self):
        """Test the default public attributes of Place."""
        obj = Place()
        attrs = [
            ("city_id", str, ""),
            ("user_id", str, ""),
            ("name", str, ""),
            ("description", str, ""),
            ("number_rooms", int, 0),
            ("number_bathrooms", int, 0),
            ("max_guest", int, 0),
            ("price_by_night", int, 0),
            ("latitude", float, 0.0),
            ("longitude", float, 0.0),
            ("amenity_ids", list, []),
        ]
        for name, typ, default in attrs:
            self.assertTrue(hasattr(obj, name))
            self.assertIsInstance(getattr(obj, name), typ)
            self.assertEqual(getattr(obj, name), default)

    def test_to_dict(self):
        """Test that to_dict reports the right class name."""
        self.assertEqual(Place().to_dict()["__class__"], "Place")

    def test_from_dict(self):
        """Test recreating Place from a dictionary."""
        a = Place()
        b = Place(**a.to_dict())
        self.assertEqual(a.id, b.id)
        self.assertIsNot(a, b)


if __name__ == "__main__":
    unittest.main()
