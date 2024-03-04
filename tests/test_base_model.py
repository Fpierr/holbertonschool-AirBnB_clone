import unittest
from models.base_model import BaseModel
from datetime import datetime
import os


class TestBaseModel(unittest.TestCase):
    def setUp(self):
        """Set up an instance of BaseModel for testing."""
        self.model = BaseModel()

    def tearDown(self):
        """Clean up after each test."""
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_instance_creation(self):
        """Test if BaseModel is correctly created."""
        self.assertIsInstance(self.model, BaseModel)
        self.assertTrue(hasattr(self.model, 'id'))
        self.assertTrue(hasattr(self.model, 'created_at'))
        self.assertTrue(hasattr(self.model, 'updated_at'))

    def test_str_representation(self):
        """Test if __str__ method returns the correct string."""
        expected_str = "[BaseModel] ({}) {}".format(
            self.model.id, self.model.__dict__)
        self.assertEqual(str(self.model), expected_str)

    def test_save_method(self):
        """Test if save method updates updated_at and calls storage save."""
        old_updated_at = self.model.updated_at
        self.model.save()
        self.assertNotEqual(old_updated_at, self.model.updated_at)
        # Check if file.json is created
        self.assertTrue(os.path.exists("file.json"))

    def test_to_dict_method(self):
        """Test if to_dict method returns the correct dictionary."""
        model_dict = self.model.to_dict()
        self.assertIsInstance(model_dict, dict)
        self.assertIn('__class__', model_dict)
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertIn('created_at', model_dict)
        self.assertIsInstance(model_dict['created_at'], str)
        self.assertIn('updated_at', model_dict)
        self.assertIsInstance(model_dict['updated_at'], str)
        self.assertIn('id', model_dict)
        self.assertIsInstance(model_dict['id'], str)

    def test_deserialization_from_dict(self):
        """Test if deserialization from dictionary works correctly."""
        model_dict = self.model.to_dict()
        new_model = BaseModel(**model_dict)
        self.assertEqual(new_model.to_dict(), model_dict)


if __name__ == '__main__':
    unittest.main()
