#!/usr/bin/python3
"""Unit tests for the Amenity class."""
import unittest
from models.base_model import BaseModel
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Test cases for Amenity."""

    def test_inheritance(self):
        """Test that Amenity inherits from BaseModel."""
        self.assertIsInstance(Amenity(), BaseModel)

    def test_attributes(self):
        """Test the default public attributes of Amenity."""
        obj = Amenity()
        for name, typ, default in [("name", str, "")]:
            self.assertTrue(hasattr(obj, name))
            self.assertIsInstance(getattr(obj, name), typ)
            self.assertEqual(getattr(obj, name), default)

    def test_to_dict(self):
        """Test that to_dict reports the right class name."""
        self.assertEqual(Amenity().to_dict()["__class__"], "Amenity")

    def test_from_dict(self):
        """Test recreating Amenity from a dictionary."""
        a = Amenity()
        b = Amenity(**a.to_dict())
        self.assertEqual(a.id, b.id)
        self.assertIsNot(a, b)


if __name__ == "__main__":
    unittest.main()
