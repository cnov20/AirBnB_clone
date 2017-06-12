#!/usr/bin/python3
import unittest
from models.amenity import Amenity


class AmenityTest(unittest.TestCase):
    """ unittest for BaseModel class"""
    def setUp(self):
        """ create a new instance """
        self.cls = Amenity()

    def testType(self):
        self.assertEqual(self.cls.__class__.__name__, "Amenity")

    def testAttributes(self):
        self.assertTrue(hasattr(self.cls, "id"))
        self.assertTrue(hasattr(self.cls, "created_at"))
        self.assertFalse(hasattr(self.cls, "updated_at"))
        self.assertFalse(hasattr(self.cls, "Holberton"))
        self.cls.school = "Holberton"
        self.cls.phno = 408505
        self.assertTrue(hasattr(self.cls, "school"))
        self.assertTrue(hasattr(self.cls, "phno"))

    def testSave(self):
        self.cls.save()
        self.assertTrue(hasattr(self.cls, "updated_at"))

    def testToJson(self):
        self.assertTrue(type(self.cls.to_json()) is dict)

if __name__ == "__main__":
    unittest.main