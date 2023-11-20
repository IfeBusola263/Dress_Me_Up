#!/usr/bin/python3
"""Creates a storage variable that is 
   answerable to all classes
"""

from models.file_storage import FileStorage


storage = FileStorage()
storage.reload()
