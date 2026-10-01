#!/usr/bin/python3
"""Unit tests for the State class."""
import unittest
from models.base_model import BaseModel
from models.state import State


class TestState(unittest.TestCase):
    """Test cases for State."""

    def test_inheritance(self):
        """Test that State inherits from BaseModel."""
        self.assertIsInstance(State(), BaseModel)

    def test_attributes(self):
        """Test the default public attributes of State."""
        obj = State()
        for name, typ, default in [("name", str, "")]:
            self.assertTrue(hasattr(obj, name))
            self.assertIsInstance(getattr(obj, name), typ)
            self.assertEqual(getattr(obj, name), default)

    def test_to_dict(self):
        """Test that to_dict reports the right class name."""
        self.assertEqual(State().to_dict()["__class__"], "State")

    def test_from_dict(self):
        """Test recreating State from a dictionary."""
        a = State()
        b = State(**a.to_dict())
        self.assertEqual(a.id, b.id)
        self.assertIsNot(a, b)


if __name__ == "__main__":
    unittest.main()
