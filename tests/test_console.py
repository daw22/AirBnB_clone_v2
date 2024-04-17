#!/usr/bin/python3
"""
tests for the console to test it's functionalities
"""
import unittest
from console import HBNBCommand
from io import StringIO
from unittest.mock import patch
from models import storage
from models.base_model import BaseModel
from models.state import State
from models.place import Place


cont = ""


class TestConsole(unittest.TestCase):
    """
    test cases for the consloe
    """

    @patch('sys.stdout', new_callable=StringIO)
    def test_create_missing_class_name(self, stdout):
        """
        tests for correct responce when class
        name is missing
        """
        HBNBCommand().do_create(None)
        expected_out = "** class name missing **\n"

        self.assertEqual(stdout.getvalue(), expected_out)

    @patch('sys.stdout', new_callable=StringIO)
    def test_create_class_name_not_found(self, stdout):
        """
        tests for non existent class name argument
        """
        HBNBCommand().do_create('wrong')
        expected_out = "** class doesn't exist **\n"

        self.assertEqual(stdout.getvalue(), expected_out)

    @patch('sys.stdout', new_callable=StringIO)
    def test_create_with_args(self, stdout):
        """
        tests create command with arguments
        """
        HBNBCommand().do_create('State name="California"')
        new_id = stdout.getvalue().strip()
        self.assertIsNotNone(new_id,
                             storage.all().get('State.{}'.format(new_id)))
        obj = storage.all().get('State.{}'.format(new_id))
        self.assertIsInstance(obj, State)
        self.assertEqual(obj.name, "California")

    @patch('sys.stdout', new_callable=StringIO)
    def test_create_with_space_args(self, stdout):
        """
        tests create command with args containing underscores
        """
        HBNBCommand().do_create('Review text="Amazing_place"')
        new_id = stdout.getvalue().strip()
        obj = storage.all().get('Review.{}'.format(new_id))
        self.assertEqual(obj.text, "Amazing place")

    @patch('sys.stdout', new_callable=StringIO)
    def test_create_with_int_and_floats(self, stdout):
        """
        tests create command with ints and floats
        """
        HBNBCommand().do_create('Place city_id="0001" user_id="0001" ' +
                                'name="My_little_house" number_rooms=4 ' +
                                'number_bathrooms=2 max_guest=10 ' +
                                'price_by_night=300 latitude=37.773972 ' +
                                'longitude=-122.431297')
        new_id = stdout.getvalue().strip()
        obj = storage.all().get('Place.{}'.format(new_id))
        self.assertIsInstance(obj.number_rooms, int)
        self.assertIsInstance(obj.number_bathrooms, int)
        self.assertIsInstance(obj.max_guest, int)
        self.assertIsInstance(obj.price_by_night, int)
        self.assertIsInstance(obj.latitude, float)
        self.assertIsInstance(obj.longitude, float)

    @patch('sys.stdout', new_callable=StringIO)
    def test_create_with_unrecognized_args(self, stdout):
        """
        tests create command with unrecognized type args
        """
        HBNBCommand().do_create('State name=["h","i"]')
        new_id = stdout.getvalue().strip()
        obj = storage.all().get('State.{}'.format(new_id))
        self.assertIsNone(obj.name)
