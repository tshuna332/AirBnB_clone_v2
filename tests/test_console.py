#!/usr/bin/python3
"""
        import modules of class PlaceTest
"""
import unittest
from unittest.mock import patch
from console import HBNBCommand
from io import StringIO
import pep8


class pep8_test(unittest.TestCase):
    """pep8 test cases class"""
    def test_pep8_conformance(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/base_model.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style Werrors (and warnings).")

class docs_test(unittest.TestCase):
    """Base model document tests"""

    def test_module_docstring(self):
        """module doc"""
        self.assertTrue(len(HBNBCommand.__doc__) >= 1)

    def test_class_docstring(self):
        """class doc"""
        self.assertTrue(len(HBNBCommand.__doc__) >= 1)

class ConsoleTest(unittest.TestCase):
    """ test cases for console"""
    def test_helpcommand(self):
        """ test cases for help command"""
        m1 = "\nDocumented commands (type help <topic>):\n"
        m2 = "========================================\n"
        m3 = "EOF  all  count  create  destroy  help  quit  show  update\n\n"
        hmsg = m1 + m2 + m3
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help randomname")
            self.assertEqual(f.getvalue(), "*** No help on randomname\n")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help quit")
            self.assertEqual(f.getvalue(), "Exits the program with formatting\n\n")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help EOF")
            self.assertEqual(f.getvalue(), "Exits the program without formatting\n\n")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help")
            self.assertEqual(f.getvalue(), hmsg)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help create")
            self.assertEqual(f.getvalue(), "Creates a class of any type\n[Usage]: create <className>\n\n")

    def test_create(self):
        """ test new command create """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create")
            self.assertEqual(f.getvalue(), "** class name missing **\n")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create ASD")
            self.assertEqual(f.getvalue(), "** class doesn't exist **\n")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all User")
            self.assertEqual(f.getvalue()[2:8], "[User]")
        with patch('sys.stdout', new=StringIO()) as f_id:
            HBNBCommand().onecmd("create User name=\"YOLO\"")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show User " + f_id.getvalue())
            self.assertTrue("'name': '\"YOLO\"'" in f.getvalue())
