#!/usr/bin/python3
""" Module for testing file storage"""
import unittest
from models.base_model import BaseModel
from models.state import State
from models import storage
import os


strg = os.getenv("HBNB_TYPE_STORAGE")


class test_fileStorage(unittest.TestCase):
    """ Class to test the file storage method """

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

    @unittest.skipIf(strg == 'db', "BaseModel not mapped to a table")
    def test_empty(self):
        """ Data is saved to file """
        new = BaseModel()
        thing = new.to_dict()
        new.save()
        new2 = BaseModel(**thing)
        self.assertNotEqual(os.path.getsize('file.json'), 0)

    @unittest.skipIf(strg == 'db', "BaseModel not mapped to a table")
    def test_save(self):
        """ FileStorage save method """
        new = BaseModel()
        storage.save()
        self.assertTrue(os.path.exists('file.json'))

    def test_reload(self):
        """ Storage file is successfully loaded to __objects """
        new = State(name='California')
        new.save()
        storage.reload()
        self.assertIsNotNone(storage.all().get("State.{}".format(new.id)))

    @unittest.skipIf(strg == 'db', "BaseModel not mapped to a table")
    def test_reload_empty(self):
        """ Load from an empty file """
        with open('file.json', 'w') as f:
            pass
        with self.assertRaises(ValueError):
            storage.reload()

    def test_reload_from_nonexistent(self):
        """ Nothing happens if file does not exist """
        self.assertEqual(storage.reload(), None)

    @unittest.skipIf(strg == 'db', "BaseModel not mapped to a table")
    def test_object_save(self):
        """ BaseModel save method calls storage save """
        new = State()
        new.save()
        self.assertTrue(os.path.exists('file.json'))

    @unittest.skipIf(strg == 'db', "BaseModel not mapped to a table")
    def test_type_path(self):
        """ Confirm __file_path is string """
        self.assertEqual(type(storage._FileStorage__file_path), str)

    def test_type_objects(self):
        """ Confirm __objects is a dict """
        self.assertEqual(type(storage.all()), dict)

    @unittest.skipIf(strg == 'db', "BaseModel not mapped to a table")
    def test_key_format(self):
        """ Key is properly formatted """
        new = State(name='California')
        storage.new(new)
        storage.save()
        _id = new.to_dict()['id']
        self.assertIsNotNone(storage.all().get('State.{}'.format(_id)))

    @unittest.skipIf(strg == 'db', "BaseModel not mapped to a table")
    def test_storage_var_created(self):
        """ FileStorage object storage created """
        from models.engine.file_storage import FileStorage
        self.assertEqual(type(storage), FileStorage)
