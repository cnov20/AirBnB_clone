#!/usr/bin/python3
import unittest
from models.state import State


class StateTest(unittest.TestCase):
    """ unittest for BaseModel class"""
    def setUp(self):
        """ create a new instance """
        self.cls = State()

    def testType(self):
        """test type"""
        self.assertEqual(self.cls.__class__.__name__, "State")

    def testAttributes(self):
        """test for attributes"""
        self.assertTrue(hasattr(self.cls, "id"))
        self.assertTrue(hasattr(self.cls, "created_at"))
        self.assertFalse(hasattr(self.cls, "updated_at"))
        self.assertFalse(hasattr(self.cls, "Holberton"))
        self.cls.school = "Holberton"
        self.cls.phno = 408505
        self.assertTrue(hasattr(self.cls, "school"))
        self.assertTrue(hasattr(self.cls, "phno"))
        self.assertTrue(hasattr(self.cls, "name"))
        self.assertEqual(self.cls.__class__.__name__, "State")
        self.assertEqual(self.cls.name, "")
        self.cls.name = "Holberton"
        self.assertEqual(self.cls.name, "Holberton")

    def testSave(self):
        """test save func"""
        self.cls.save()
        self.assertTrue(hasattr(self.cls, "updated_at"))

    def testToJson(self):
        """test json"""
        self.assertTrue(type(self.cls.to_json()) is dict)

if __name__ == "__main__":
    unittest.main
