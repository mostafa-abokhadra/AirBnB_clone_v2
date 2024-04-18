#!/usr/bin/python3
"""__init__ file for the Storage system"""
from models.engine.file_storage import FileStorage
from os import getenv
from models.city import City
from models.place import Place
from models.state import State
from models.user import User
from models.review import Review
from models.amenity import Amenity
from models.engine.db_storage import DBStorage


if getenv('HBNB_TYPE_STORAGE') == 'db':
    storage = DBStorage()
else:
    storage = FileStorage()

storage.reload()
