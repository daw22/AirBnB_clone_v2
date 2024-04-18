#!/usr/bin/python3
""" """
import os
from tests.test_models.test_base_model import test_basemodel
from models.state import State


strg = os.getenv("HBNB_TYPE_STORAGE")


class test_state(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ Initializes the test """
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_name3(self):
        """ tests name """
        new = self.value()
        self.assertIsNone(new.name)
        new = self.value(name="Texas")
        self.assertEqual(new.name, "Texas")
