#!/usr/bin/python3
"""Creates a storage variable that is 
   answerable to all classes
"""

from os import getenv

storage_type = getenv("DRESS_ME_TYPE_STORAGE")

if storage_type == 'db':
    from models.engine.db_storage import DBStorage
    storage = DBStorage()

else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()

storage.reload()
