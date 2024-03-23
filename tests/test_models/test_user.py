#!/usr/bin/python3
"""
Unnitest for user.py
"""
import unittest
from models.user import User
from models.base_model import BaseModel
from datetime import datetime


class UserCase(unittest.TestCase):
    """Tests instances and methods from user class"""
    user = User()

    def test_class_exist(self):
        self.assertEqual(str(type(self.user)), "<class 'models.user.User'>")

    def test_user_inheritance(self):
        """test if User is a subclass of BaseModel"""
        self.assertIsInstance(self.user, User)

    def testHasAttributes(self):
        """verify if attributes exist"""
        self.assertTrue(hasattr(self.user, 'email'))
        self.assertTrue(hasattr(self.user, 'password'))
        self.assertTrue(hasattr(self.user, 'first_name'))
        self.assertTrue(hasattr(self.user, 'last_name'))
        self.assertTrue(hasattr(self.user, 'id'))
        self.assertTrue(hasattr(self.user, 'created_at'))
        self.assertTrue(hasattr(self.user, 'updated_at'))

    def test_types(self):
        """tests if the type of the attribute is the correct one"""
        self.assertIsInstance(self.user.email, str)
        self.assertIsInstance(self.user.password, str)
        self.assertIsInstance(self.user.first_name, str)
        self.assertIsInstance(self.user.last_name, str)
        self.assertIsInstance(self.user.id, str)
        self.assertIsInstance(self.user.created_at, datetime)
        self.assertIsInstance(self.user.updated_at, datetime)


if __name__ == '__main__':
    unittest.main()
