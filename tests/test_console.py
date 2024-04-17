#!/usr/bin/python3
"""
tests for the console to test it's functionalities
"""
import unittest
from console import HBNBCommand
from io import StringIO
from unittest.mock import patch
from models.base_model import BaseModel
from models.state import State
from models.place import Place


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
