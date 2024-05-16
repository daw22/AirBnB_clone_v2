#!/usr/bin/python3
"""
__init__ file for the models package
"""
import os


if os.getenv("HBNB_TYPE_STORAGE") == "db":
    import models.engine.db_storage as db_storage
    storage = db_storage.DBStorage()
else:
    import models.engine.file_storage as file_storage
    storage = file_storage.FileStorage()
storage.reload()
