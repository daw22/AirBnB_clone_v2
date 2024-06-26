#!/usr/bin/python3
"""
contains

classes:
    TestHBNBCommand - unittest test cases for the HBNBCommand class/the console
"""
import io
import sys
import unittest
from console import HBNBCommand
from models import storage
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class TestHBNBCommand(unittest.TestCase):
    """
    Contains test cases for the HBNBCommand class.
    """
    def setUp(self):
        """
        Set up code executed once before every test/method.
        """
        self.cmd = HBNBCommand()
        self.base = BaseModel()
        self.user = User()
        self.state = State()
        self.city = City()
        self.amenity = Amenity()
        self.place = Place()
        self.review = Review()

        self.base.save()
        self.user.save()
        self.state.save()
        self.city.save()
        self.amenity.save()
        self.place.save()
        self.review.save()

    def test_help(self):
        """
        Tests the help command.
        """
        w_space = "\n        {}\n        \n"

        # Tests -> help quit
        output = io.StringIO()
        sys.stdout = output
        self.cmd.onecmd("help quit")
        text = "Quits the command line interpreter\n"
        self.assertEqual(output.getvalue(), text)
        output.close()

        # Tests -> help EOF
        output = io.StringIO()
        sys.stdout = output
        self.cmd.onecmd("help EOF")
        text = "Exits the command line interpreter (when ctrl+d is clicked)\n"
        self.assertEqual(output.getvalue(), text)
        output.close()

        # Tests -> help create
        output = io.StringIO()
        sys.stdout = output
        HBNBCommand().onecmd("help create")
        text = "creates a new instance and prints it's id"
        self.assertEqual(output.getvalue(), w_space.format(text))
        output.close()

        # Tests -> help show
        output = io.StringIO()
        sys.stdout = output
        HBNBCommand().onecmd("help show")
        text = "loads and prints the string representation of an instance"
        self.assertEqual(output.getvalue(), w_space.format(text))
        output.close()

        # Tests -> help destroy
        output = io.StringIO()
        sys.stdout = output
        HBNBCommand().onecmd("help destroy")
        text = "Destroys a class instance with a given ID."
        self.assertEqual(output.getvalue(), w_space.format(text))
        output.close()

        # Tests -> help all
        output = io.StringIO()
        sys.stdout = output
        HBNBCommand().onecmd("help all")
        tmp = "of all instances of a model."
        text = "Loads and prints the string representation " + tmp
        self.assertEqual(output.getvalue(), w_space.format(text))
        output.close()

        # Tests -> help update
        output = io.StringIO()
        sys.stdout = output
        HBNBCommand().onecmd("help update")
        text = "Updates a given attribute of an instance of a given class."
        self.assertEqual(output.getvalue(), w_space.format(text))
        output.close()

        # Tests -> help count
        output = io.StringIO()
        sys.stdout = output
        HBNBCommand().onecmd("help count")
        text = "counts the number of instance of a particular class"
        self.assertEqual(output.getvalue(), w_space.format(text))
        output.close()

    def test_quit(self):
        """
        Tests the quit command of the HBNBCommand class.
        """
        output = io.StringIO()
        sys.stdout = output
        val = self.cmd.onecmd("quit")
        self.assertEqual(output.getvalue(), '')

    def test_EOF(self):
        """
        Tests the EOF (ctrl d) command of the HBNBCommand class.
        """
        output = io.StringIO()
        sys.stdout = output
        val = self.cmd.onecmd("EOF")
        self.assertEqual(output.getvalue(), '')

    def test_empty_line(self):
        """
        Tests the console (HBNBCommand) when an empty line is given as input.
        """
        output = io.StringIO()
        sys.stdout = output
        val = self.cmd.onecmd("")
        self.assertEqual(output.getvalue(), '')

    def test_create(self):
        """
        Tests the create command of the HBNBCommand.
        """
        output = io.StringIO()
        sys.stdout = output
        self.cmd.onecmd("create BaseModel")
        key = "BaseModel.{}".format(output.getvalue().strip())
        self.assertTrue(key in storage.all())
        self.assertIsInstance(storage.all()[key], BaseModel)

        output = io.StringIO()
        sys.stdout = output
        self.cmd.onecmd("create User")
        key = "User.{}".format(output.getvalue().strip())
        self.assertTrue(key in storage.all())
        self.assertIsInstance(storage.all()[key], User)

        output = io.StringIO()
        sys.stdout = output
        self.cmd.onecmd("create State")
        key = "State.{}".format(output.getvalue().strip())
        self.assertTrue(key in storage.all())
        self.assertIsInstance(storage.all()[key], State)

        output = io.StringIO()
        sys.stdout = output
        self.cmd.onecmd("create City")
        key = "City.{}".format(output.getvalue().strip())
        self.assertTrue(key in storage.all())
        self.assertIsInstance(storage.all()[key], City)

        output = io.StringIO()
        sys.stdout = output
        self.cmd.onecmd("create Amenity")
        key = "Amenity.{}".format(output.getvalue().strip())
        self.assertTrue(key in storage.all())
        self.assertIsInstance(storage.all()[key], Amenity)

        output = io.StringIO()
        sys.stdout = output
        self.cmd.onecmd("create Place")
        key = "Place.{}".format(output.getvalue().strip())
        self.assertTrue(key in storage.all())
        self.assertIsInstance(storage.all()[key], Place)

        output = io.StringIO()
        sys.stdout = output
        self.cmd.onecmd("create Review")
        key = "Review.{}".format(output.getvalue().strip())
        self.assertTrue(key in storage.all())
        self.assertIsInstance(storage.all()[key], Review)

    def test_create_with_str_params(self):
        """
        Tests the create command with string arguments to the object's init
        """
        output = io.StringIO()
        sys.stdout = output
        self.cmd.onecmd('create State name="Arizona"')
        key = "State.{}".format(output.getvalue().strip())
        self.assertTrue(key in storage.all())
        state = storage.all()[key]
        self.assertIsInstance(state, State)
        self.assertIsInstance(state.name, str)
        self.assertEqual(state.name, "Arizona")

    def test_create_with_spaced_str(self):
        """
        Tests the create command's underscore -> space replacement
        """
        output = io.StringIO()
        sys.stdout = output
        self.cmd.onecmd('create State name="A_place_far_away"')
        key = "State.{}".format(output.getvalue().strip())
        self.assertTrue(key in storage.all())
        state = storage.all()[key]
        self.assertIsInstance(state, State)
        self.assertIsInstance(state.name, str)
        self.assertEqual(state.name, "A place far away")

    def test_create_with_int_params(self):
        """
        Tests the create command with integer arguments to the object's init
        """
        output = io.StringIO()
        sys.stdout = output
        self.cmd.onecmd('create Place max_guest=10')
        key = "Place.{}".format(output.getvalue().strip())
        self.assertTrue(key in storage.all())
        place = storage.all()[key]
        self.assertIsInstance(place, Place)
        self.assertIsInstance(place.max_guest, int)
        self.assertEqual(place.max_guest, 10)

    def test_create_with_float_params(self):
        """
        Tests the create command with float arguments to the object's init
        """
        output = io.StringIO()
        sys.stdout = output
        self.cmd.onecmd('create Place latitude=37.773972')
        key = "Place.{}".format(output.getvalue().strip())
        self.assertTrue(key in storage.all())
        place = storage.all()[key]
        self.assertIsInstance(place, Place)
        self.assertIsInstance(place.latitude, float)
        self.assertAlmostEqual(place.latitude, 37.773972)

    def test_create_with_multiple_params(self):
        """
        Tests the create command with multiple parameters to the object's init
        """
        output = io.StringIO()
        sys.stdout = output
        self.cmd.onecmd('create Place city_id="0001" user_id="0001"' +
                        ' name="My_little_house" number_rooms=4' +
                        ' number_bathrooms=2 max_guest=10 price_by_night=300' +
                        ' latitude=37.773972 longitude=-122.431297')
        key = "Place.{}".format(output.getvalue().strip())
        self.assertTrue(key in storage.all())
        place = storage.all()[key]
        self.assertIsInstance(place, Place)
        self.assertEqual(place.city_id, "0001")
        self.assertEqual(place.user_id, "0001")
        self.assertEqual(place.name, "My little house")
        self.assertEqual(place.number_rooms, 4)
        self.assertEqual(place.number_bathrooms, 2)
        self.assertEqual(place.max_guest, 10)
        self.assertEqual(place.price_by_night, 300)
        self.assertAlmostEqual(place.latitude, 37.773972)
        self.assertAlmostEqual(place.longitude, -122.431297)

    def test_create_invalid_args(self):
        """
        Tests the create command of the HBNBCommand class with invalid args.
        """
        output = io.StringIO()
        sys.stdout = output
        self.cmd.onecmd("create")
        self.assertEqual(output.getvalue(), "** class name missing **\n")

        output = io.StringIO()
        sys.stdout = output
        self.cmd.onecmd("create Random")
        self.assertEqual(output.getvalue(), "** class doesn't exist **\n")

    def test_show(self):
        """
        Tests the show command of HBNBCommand class.
        """
        output = io.StringIO()
        sys.stdout = output
        self.cmd.onecmd("show BaseModel {}".format(self.base.id))
        self.assertEqual(output.getvalue(), str(self.base) + '\n')

        output = io.StringIO()
        sys.stdout = output
        self.cmd.onecmd("show User {}".format(self.user.id))
        self.assertEqual(output.getvalue(), str(self.user) + '\n')

        output = io.StringIO()
        sys.stdout = output
        self.cmd.onecmd("show State {}".format(self.state.id))
        self.assertEqual(output.getvalue(), str(self.state) + '\n')

        output = io.StringIO()
        sys.stdout = output
        self.cmd.onecmd("show City {}".format(self.city.id))
        self.assertEqual(output.getvalue(), str(self.city) + '\n')

        output = io.StringIO()
        sys.stdout = output
        self.cmd.onecmd("show Amenity {}".format(self.amenity.id))
        self.assertEqual(output.getvalue(), str(self.amenity) + '\n')

        output = io.StringIO()
        sys.stdout = output
        self.cmd.onecmd("show Place {}".format(self.place.id))
        self.assertEqual(output.getvalue(), str(self.place) + '\n')

        output = io.StringIO()
        sys.stdout = output
        self.cmd.onecmd("show Review {}".format(self.review.id))
        self.assertEqual(output.getvalue(), str(self.review) + '\n')

    def test_show_dot(self):
        """
        Tests the show command with the dot notation (Classname.show(id)).
        """
        output = io.StringIO()
        sys.stdout = output
        self.cmd.onecmd("BaseModel.show({})".format(self.base.id))
        self.assertEqual(output.getvalue(), str(self.base) + '\n')

        output = io.StringIO()
        sys.stdout = output
        self.cmd.onecmd("User.show({})".format(self.user.id))
        self.assertEqual(output.getvalue(), str(self.user) + '\n')

        output = io.StringIO()
        sys.stdout = output
        self.cmd.onecmd("State.show({})".format(self.state.id))
        self.assertEqual(output.getvalue(), str(self.state) + '\n')

        output = io.StringIO()
        sys.stdout = output
        self.cmd.onecmd("City.show({})".format(self.city.id))
        self.assertEqual(output.getvalue(), str(self.city) + '\n')

        output = io.StringIO()
        sys.stdout = output
        self.cmd.onecmd("Amenity.show({})".format(self.amenity.id))
        self.assertEqual(output.getvalue(), str(self.amenity) + '\n')

        output = io.StringIO()
        sys.stdout = output
        self.cmd.onecmd("Place.show({})".format(self.place.id))
        self.assertEqual(output.getvalue(), str(self.place) + '\n')

        output = io.StringIO()
        sys.stdout = output
        self.cmd.onecmd("Review.show({})".format(self.review.id))
        self.assertEqual(output.getvalue(), str(self.review) + '\n')

    def test_show_invalid_args(self):
        """
        Tests the show command of the HBNBCommand class with invalid args.
        """
        output = io.StringIO()
        sys.stdout = output
        self.cmd.onecmd("show")
        self.assertEqual(output.getvalue(), "** class name missing **\n")

        output = io.StringIO()
        sys.stdout = output
        self.cmd.onecmd("show Random")
        self.assertEqual(output.getvalue(), "** class doesn't exist **\n")

        output = io.StringIO()
        sys.stdout = output
        self.cmd.onecmd("Random.show()")
        self.assertEqual(output.getvalue(), "** class doesn't exist **\n")

        output = io.StringIO()
        sys.stdout = output
        self.cmd.onecmd("show BaseModel")
        self.assertEqual(output.getvalue(), "** instance id missing **\n")

        output = io.StringIO()
        sys.stdout = output
        self.cmd.onecmd("BaseModel.show()")
        self.assertEqual(output.getvalue(), "** instance id missing **\n")

        output = io.StringIO()
        sys.stdout = output
        self.cmd.onecmd("show User 1234-4321-1234-4321")
        self.assertEqual(output.getvalue(), "** no instance found **\n")

        output = io.StringIO()
        sys.stdout = output
        self.cmd.onecmd("User.show(1234-4321-1234-4321)")
        self.assertEqual(output.getvalue(), "** no instance found **\n")

    def test_destroy(self):
        """
        Tests the destroy command of the HBNBCommand class.
        """
        key = "BaseModel.{}".format(self.base.id)
        self.assertTrue(key in storage.all())
        self.cmd.onecmd("destroy BaseModel {}".format(self.base.id))
        self.assertFalse(key in storage.all())

        key = "User.{}".format(self.user.id)
        self.assertTrue(key in storage.all())
        self.cmd.onecmd("destroy User {}".format(self.user.id))
        self.assertFalse(key in storage.all())

        key = "State.{}".format(self.state.id)
        self.assertTrue(key in storage.all())
        self.cmd.onecmd("destroy State {}".format(self.state.id))
        self.assertFalse(key in storage.all())

        key = "City.{}".format(self.city.id)
        self.assertTrue(key in storage.all())
        self.cmd.onecmd("destroy City {}".format(self.city.id))
        self.assertFalse(key in storage.all())

        key = "Amenity.{}".format(self.amenity.id)
        self.assertTrue(key in storage.all())
        self.cmd.onecmd("destroy Amenity {}".format(self.amenity.id))
        self.assertFalse(key in storage.all())

        key = "Place.{}".format(self.place.id)
        self.assertTrue(key in storage.all())
        self.cmd.onecmd("destroy Place {}".format(self.place.id))
        self.assertFalse(key in storage.all())

        key = "Review.{}".format(self.review.id)
        self.assertTrue(key in storage.all())
        self.cmd.onecmd("destroy Review {}".format(self.review.id))
        self.assertFalse(key in storage.all())

    def test_destroy_dot(self):
        """
        Tests the destroy command with dot notation (Classname.destroy(id)).
        """
        key = "BaseModel.{}".format(self.base.id)
        self.assertTrue(key in storage.all())
        self.cmd.onecmd("BaseModel.destroy({})".format(self.base.id))
        self.assertFalse(key in storage.all())

        key = "User.{}".format(self.user.id)
        self.assertTrue(key in storage.all())
        self.cmd.onecmd("User.destroy({})".format(self.user.id))
        self.assertFalse(key in storage.all())

        key = "State.{}".format(self.state.id)
        self.assertTrue(key in storage.all())
        self.cmd.onecmd("State.destroy({})".format(self.state.id))
        self.assertFalse(key in storage.all())

        key = "City.{}".format(self.city.id)
        self.assertTrue(key in storage.all())
        self.cmd.onecmd("City.destroy({})".format(self.city.id))
        self.assertFalse(key in storage.all())

        key = "Amenity.{}".format(self.amenity.id)
        self.assertTrue(key in storage.all())
        self.cmd.onecmd("Amenity.destroy({})".format(self.amenity.id))
        self.assertFalse(key in storage.all())

        key = "Place.{}".format(self.place.id)
        self.assertTrue(key in storage.all())
        self.cmd.onecmd("Place.destroy({})".format(self.place.id))
        self.assertFalse(key in storage.all())

        key = "Review.{}".format(self.review.id)
        self.assertTrue(key in storage.all())
        self.cmd.onecmd("Review.destroy({})".format(self.review.id))
        self.assertFalse(key in storage.all())

    def test_destroy_invalid_args(self):
        """
        Tests the destroy command of the HBNBCommand class with invalid args.
        """
        output = io.StringIO()
        sys.stdout = output
        self.cmd.onecmd("destroy")
        self.assertEqual(output.getvalue(), "** class name missing **\n")

        output = io.StringIO()
        sys.stdout = output
        self.cmd.onecmd("destroy Random")
        self.assertEqual(output.getvalue(), "** class doesn't exist **\n")

        output = io.StringIO()
        sys.stdout = output
        self.cmd.onecmd("Random.destroy()")
        self.assertEqual(output.getvalue(), "** class doesn't exist **\n")

        output = io.StringIO()
        sys.stdout = output
        self.cmd.onecmd("destroy BaseModel")
        self.assertEqual(output.getvalue(), "** instance id missing **\n")

        output = io.StringIO()
        sys.stdout = output
        self.cmd.onecmd("BaseModel.destroy()")
        self.assertEqual(output.getvalue(), "** instance id missing **\n")

        output = io.StringIO()
        sys.stdout = output
        self.cmd.onecmd("destroy User 1234-4321-1234-4321")
        self.assertEqual(output.getvalue(), "** no instance found **\n")

        output = io.StringIO()
        sys.stdout = output
        self.cmd.onecmd("User.destroy(1234-4321-1234-4321)")
        self.assertEqual(output.getvalue(), "** no instance found **\n")

    def test_all(self):
        """
        Tests the all command of the HBNBCommand class.
        """
        objs = storage.all().values()

        output = io.StringIO()
        sys.stdout = output
        self.cmd.onecmd("all")
        objs_lst = [str(obj) for obj in objs]
        self.assertEqual(output.getvalue(), str(objs_lst) + '\n')

        output = io.StringIO()
        sys.stdout = output
        self.cmd.onecmd("all BaseModel")
        objs_lst = [str(obj) for obj in objs if type(obj) is BaseModel]
        self.assertEqual(output.getvalue(), str(objs_lst) + '\n')

        output = io.StringIO()
        sys.stdout = output
        self.cmd.onecmd("all User")
        objs_lst = [str(obj) for obj in objs if type(obj) is User]
        self.assertEqual(output.getvalue(), str(objs_lst) + '\n')

        output = io.StringIO()
        sys.stdout = output
        self.cmd.onecmd("all State")
        objs_lst = [str(obj) for obj in objs if type(obj) is State]
        self.assertEqual(output.getvalue(), str(objs_lst) + '\n')

        output = io.StringIO()
        sys.stdout = output
        self.cmd.onecmd("all City")
        objs_lst = [str(obj) for obj in objs if type(obj) is City]
        self.assertEqual(output.getvalue(), str(objs_lst) + '\n')

        output = io.StringIO()
        sys.stdout = output
        self.cmd.onecmd("all Amenity")
        objs_lst = [str(obj) for obj in objs if type(obj) is Amenity]
        self.assertEqual(output.getvalue(), str(objs_lst) + '\n')

        output = io.StringIO()
        sys.stdout = output
        self.cmd.onecmd("all Place")
        objs_lst = [str(obj) for obj in objs if type(obj) is Place]
        self.assertEqual(output.getvalue(), str(objs_lst) + '\n')

        output = io.StringIO()
        sys.stdout = output
        self.cmd.onecmd("all Review")
        objs_lst = [str(obj) for obj in objs if type(obj) is Review]
        self.assertEqual(output.getvalue(), str(objs_lst) + '\n')

    def test_all_dot(self):
        """
        Tests the all command with the dot notation (Classname.all()).
        """
        objs = storage.all().values()

        output = io.StringIO()
        sys.stdout = output
        self.cmd.onecmd("BaseModel.all()")
        objs_lst = [str(obj) for obj in objs if type(obj) is BaseModel]
        self.assertEqual(output.getvalue(), str(objs_lst) + '\n')

        output = io.StringIO()
        sys.stdout = output
        self.cmd.onecmd("User.all()")
        objs_lst = [str(obj) for obj in objs if type(obj) is User]
        self.assertEqual(output.getvalue(), str(objs_lst) + '\n')

        output = io.StringIO()
        sys.stdout = output
        self.cmd.onecmd("State.all()")
        objs_lst = [str(obj) for obj in objs if type(obj) is State]
        self.assertEqual(output.getvalue(), str(objs_lst) + '\n')

        output = io.StringIO()
        sys.stdout = output
        self.cmd.onecmd("City.all()")
        objs_lst = [str(obj) for obj in objs if type(obj) is City]
        self.assertEqual(output.getvalue(), str(objs_lst) + '\n')

        output = io.StringIO()
        sys.stdout = output
        self.cmd.onecmd("Amenity.all()")
        objs_lst = [str(obj) for obj in objs if type(obj) is Amenity]
        self.assertEqual(output.getvalue(), str(objs_lst) + '\n')

        output = io.StringIO()
        sys.stdout = output
        self.cmd.onecmd("Place.all()")
        objs_lst = [str(obj) for obj in objs if type(obj) is Place]
        self.assertEqual(output.getvalue(), str(objs_lst) + '\n')

        output = io.StringIO()
        sys.stdout = output
        self.cmd.onecmd("Review.all()")
        objs_lst = [str(obj) for obj in objs if type(obj) is Review]
        self.assertEqual(output.getvalue(), str(objs_lst) + '\n')

    def test_all_invalid_args(self):
        """
        Tests the all command of the HBNBCommand class woth invalid args.
        """
        output = io.StringIO()
        sys.stdout = output
        self.cmd.onecmd("all Random")
        self.assertEqual(output.getvalue(), "** class doesn't exist **\n")

        output = io.StringIO()
        sys.stdout = output
        self.cmd.onecmd("Random.all()")
        self.assertEqual(output.getvalue(), "** class doesn't exist **\n")

    def test_update(self):
        """
        Tests the update command of the HBNBCommand class.
        """
        self.cmd.onecmd("update BaseModel {} name base".format(self.base.id))
        self.assertEqual(self.base.name, "base")

        self.cmd.onecmd("update User {} password pwd".format(self.user.id))
        self.assertEqual(self.user.password, "pwd")

        self.cmd.onecmd("update State {} name Arizona".format(self.state.id))
        self.assertEqual(self.state.name, "Arizona")

        command = "update City {} state_id {}"
        self.cmd.onecmd(command.format(self.city.id, self.state.id))
        self.assertEqual(self.city.state_id, self.state.id)

        self.cmd.onecmd("update Amenity {} name Pool".format(self.amenity.id))
        self.assertEqual(self.amenity.name, "Pool")

        command = "update Place {} city_id {}"
        self.cmd.onecmd(command.format(self.place.id, self.city.id))
        self.assertEqual(self.place.city_id, self.city.id)

        command = "update Review {} user_id {}"
        self.cmd.onecmd(command.format(self.review.id, self.user.id))
        self.assertEqual(self.review.user_id, self.user.id)

    def test_update_dot(self):
        """
        Tests the update command with the dot notation (Classname.update(...)).
        """
        command = "BaseModel.update({}, name, base)"
        self.cmd.onecmd(command.format(self.base.id))
        self.assertEqual(self.base.name, "base")

        command = "User.update({}, password, pwd)"
        self.cmd.onecmd(command.format(self.user.id))
        self.assertEqual(self.user.password, "pwd")

        command = "State.update({}, name, Arizona)"
        self.cmd.onecmd(command.format(self.state.id))
        self.assertEqual(self.state.name, "Arizona")

        command = "City.update({}, state_id, {})"
        self.cmd.onecmd(command.format(self.city.id, self.state.id))
        self.assertEqual(self.city.state_id, self.state.id)

        command = "Amenity.update({}, name, Pad)"
        self.cmd.onecmd(command.format(self.amenity.id))
        self.assertEqual(self.amenity.name, "Pad")

        command = "Place.update({}, city_id, {})"
        self.cmd.onecmd(command.format(self.place.id, self.city.id))
        self.assertEqual(self.place.city_id, self.city.id)

        command = "Review.update({}, user_id, {})"
        self.cmd.onecmd(command.format(self.review.id, self.user.id))
        self.assertEqual(self.review.user_id, self.user.id)

    def test_update_dict(self):
        """
        Tests the update command with a dictionary arg which is

             Classname.update(id, {attr1_name: val1, attr2_name: val2, ...}))

        """
        command = "BaseModel.update({}, {{name: base, area: London}})"
        self.cmd.onecmd(command.format(self.base.id))
        self.assertEqual(self.base.name, "base")
        self.assertEqual(self.base.area, "London")

        command = "User.update({}, {{password: pwd}})"
        self.cmd.onecmd(command.format(self.user.id))
        self.assertEqual(self.user.password, "pwd")

        self.cmd.onecmd("State.update({}, {{name: Az)}}".format(self.state.id))
        self.assertEqual(self.state.name, "Az")

        command = "City.update({}, {{state_id: {}}})"
        self.cmd.onecmd(command.format(self.city.id, self.state.id))
        self.assertEqual(self.city.state_id, self.state.id)

        command = "Amenity.update({}, {{name: Padio}})"
        self.cmd.onecmd(command.format(self.amenity.id))
        self.assertEqual(self.amenity.name, "Padio")

        command = "Place.update({}, {{city_id: {}}})"
        self.cmd.onecmd(command.format(self.place.id, self.city.id))
        self.assertEqual(self.place.city_id, self.city.id)

        command = "Review.update({}, {{user_id: {}}})"
        self.cmd.onecmd(command.format(self.review.id, self.user.id))
        self.assertEqual(self.review.user_id, self.user.id)

    def test_update_invalid_args(self):
        """
        Tests the update command of the HBNBCommand class with invalid args.
        """
        output = io.StringIO()
        sys.stdout = output
        self.cmd.onecmd("update")
        self.assertEqual(output.getvalue(), "** class name missing **\n")

        output = io.StringIO()
        sys.stdout = output
        self.cmd.onecmd("update Random")
        self.assertEqual(output.getvalue(), "** class doesn't exist **\n")

        output = io.StringIO()
        sys.stdout = output
        self.cmd.onecmd("Random.update()")
        self.assertEqual(output.getvalue(), "** class doesn't exist **\n")

        output = io.StringIO()
        sys.stdout = output
        self.cmd.onecmd("update BaseModel")
        self.assertEqual(output.getvalue(), "** instance id missing **\n")

        output = io.StringIO()
        sys.stdout = output
        self.cmd.onecmd("BaseModel.update()")
        self.assertEqual(output.getvalue(), "** instance id missing **\n")

        output = io.StringIO()
        sys.stdout = output
        self.cmd.onecmd("update User 1234-4321-1234-4321")
        self.assertEqual(output.getvalue(), "** no instance found **\n")

        output = io.StringIO()
        sys.stdout = output
        self.cmd.onecmd("User.update(1234-4321-1234-4321)")
        self.assertEqual(output.getvalue(), "** no instance found **\n")

        output = io.StringIO()
        sys.stdout = output
        self.cmd.onecmd("update User {}".format(self.user.id))
        self.assertEqual(output.getvalue(), "** attribute name missing **\n")

        output = io.StringIO()
        sys.stdout = output
        self.cmd.onecmd("User.update({})".format(self.user.id))
        self.assertEqual(output.getvalue(), "** attribute name missing **\n")

        output = io.StringIO()
        sys.stdout = output
        self.cmd.onecmd("update User {} first_name".format(self.user.id))
        self.assertEqual(output.getvalue(), "** value missing **\n")

        output = io.StringIO()
        sys.stdout = output
        self.cmd.onecmd("User.update({}, first_name)".format(self.user.id))
        self.assertEqual(output.getvalue(), "** value missing **\n")

    def test_count(self):
        """
        Tests the count command of the HBNBCommand class.
        """
        objs = storage.all().values()

        output = io.StringIO()
        sys.stdout = output
        self.cmd.onecmd("count BaseModel")
        objs_lst = [str(obj) for obj in objs if type(obj) is BaseModel]
        self.assertEqual(output.getvalue(), str(len(objs_lst)) + '\n')

        output = io.StringIO()
        sys.stdout = output
        self.cmd.onecmd("count User")
        objs_lst = [str(obj) for obj in objs if type(obj) is User]
        self.assertEqual(output.getvalue(), str(len(objs_lst)) + '\n')

        output = io.StringIO()
        sys.stdout = output
        self.cmd.onecmd("count State")
        objs_lst = [str(obj) for obj in objs if type(obj) is State]
        self.assertEqual(output.getvalue(), str(len(objs_lst)) + '\n')

        output = io.StringIO()
        sys.stdout = output
        self.cmd.onecmd("count City")
        objs_lst = [str(obj) for obj in objs if type(obj) is City]
        self.assertEqual(output.getvalue(), str(len(objs_lst)) + '\n')

        output = io.StringIO()
        sys.stdout = output
        self.cmd.onecmd("count Amenity")
        objs_lst = [str(obj) for obj in objs if type(obj) is Amenity]
        self.assertEqual(output.getvalue(), str(len(objs_lst)) + '\n')

        output = io.StringIO()
        sys.stdout = output
        self.cmd.onecmd("count Place")
        objs_lst = [str(obj) for obj in objs if type(obj) is Place]
        self.assertEqual(output.getvalue(), str(len(objs_lst)) + '\n')

        output = io.StringIO()
        sys.stdout = output
        self.cmd.onecmd("count Review")
        objs_lst = [str(obj) for obj in objs if type(obj) is Review]
        self.assertEqual(output.getvalue(), str(len(objs_lst)) + '\n')

    def test_count_dot(self):
        """
        Tests the count command with the dot notation (Classname.count()).
        """
        objs = storage.all().values()

        output = io.StringIO()
        sys.stdout = output
        self.cmd.onecmd("BaseModel.count()")
        objs_lst = [str(obj) for obj in objs if type(obj) is BaseModel]
        self.assertEqual(output.getvalue(), str(len(objs_lst)) + '\n')

        output = io.StringIO()
        sys.stdout = output
        self.cmd.onecmd("User.count()")
        objs_lst = [str(obj) for obj in objs if type(obj) is User]
        self.assertEqual(output.getvalue(), str(len(objs_lst)) + '\n')

        output = io.StringIO()
        sys.stdout = output
        self.cmd.onecmd("State.count()")
        objs_lst = [str(obj) for obj in objs if type(obj) is State]
        self.assertEqual(output.getvalue(), str(len(objs_lst)) + '\n')

        output = io.StringIO()
        sys.stdout = output
        self.cmd.onecmd("City.count()")
        objs_lst = [str(obj) for obj in objs if type(obj) is City]
        self.assertEqual(output.getvalue(), str(len(objs_lst)) + '\n')

        output = io.StringIO()
        sys.stdout = output
        self.cmd.onecmd("Amenity.count()")
        objs_lst = [str(obj) for obj in objs if type(obj) is Amenity]
        self.assertEqual(output.getvalue(), str(len(objs_lst)) + '\n')

        output = io.StringIO()
        sys.stdout = output
        self.cmd.onecmd("Place.count()")
        objs_lst = [str(obj) for obj in objs if type(obj) is Place]
        self.assertEqual(output.getvalue(), str(len(objs_lst)) + '\n')

        output = io.StringIO()
        sys.stdout = output
        self.cmd.onecmd("Review.count()")
        objs_lst = [str(obj) for obj in objs if type(obj) is Review]
        self.assertEqual(output.getvalue(), str(len(objs_lst)) + '\n')

    @classmethod
    def tearDownClass(cls):
        """
        Teardown method of the class, returns standard output to proper stream.
        """
        sys.stdout = sys.__stdout__
