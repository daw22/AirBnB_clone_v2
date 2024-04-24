#!/usr/bin/python3
"""

Test file for db storage

"""
import os
import unittest
from models import storage
from models.base_model import BaseModel
from models.state import State


strg = os.getenv("HBNB_TYPE_STORAGE")


class test_dbStorage(unittest.TestCase):
    """Tests db storage of the application"""

    def setUp(self):
        """ Set up test environment """
        del_list = []
        if strg != 'db':
            for key in storage._FileStorage__objects.keys():
                del_list.append(key)
            for key in del_list:
                del storage._FileStorage__objects[key]

    def tearDown(self):
        """ Remove storage file at end of tests """
        try:
            os.remove('file.json')
        except Exception:
            pass

    @unittest.skipIf(strg == 'db', "No __objects")
    def test_obj_list_empty(self):
        """ __objects is initially empty """
        self.assertEqual(len(storage.all()), 0)

    def test_new(self):
        """ New object is correctly added to __objects """
        new = State(name='California')
        storage.new(new)
        obj = storage.all().get('State.{}'.format(new.id))
        self.assertTrue(new is obj)

    def test_all(self):
        """ __objects is properly returned """
        new = BaseModel()
        temp = storage.all()
        self.assertIsInstance(temp, dict)

    def test_base_model_instantiation(self):
        """ File is not created on BaseModel save """
        new = BaseModel()
        self.assertFalse(os.path.exists('file.json'))

    def test_reload(self):
        """ Storage file is successfully loaded to __objects """
        new = State(name='California')
        new.save()
        storage.reload()
        self.assertIsNotNone(storage.all().get("State.{}".format(new.id)))

    def test_reload_from_nonexistent(self):
        """ Nothing happens if file does not exist """
        self.assertEqual(storage.reload(), None)

    @unittest.skipIf(strg == 'db', "BaseModel not mapped to a table")
    def test_type_path(self):
        """ Confirm __file_path is string """
        self.assertEqual(type(storage._FileStorage__file_path), str)

    def test_type_objects(self):
        """ Confirm __objects is a dict """
        self.assertEqual(type(storage.all()), dict)

    def test_key_format(self):
        """ Key is properly formatted """
        new = State(name='California')
        storage.new(new)
        storage.save()
        _id = new.to_dict()['id']
        self.assertIsNotNone(storage.all().get('State.{}'.format(_id)))

    @unittest.skipIf(strg != 'db', "FileStorage created in that case")
    def test_storage_var_created(self):
        """ DBStorage object storage created """
        from models.engine.db_storage import DBStorage
        self.assertEqual(type(storage), DBStorage)
