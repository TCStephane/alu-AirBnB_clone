#!/usr/bin/python3
"""Package initializer that creates the unique FileStorage instance."""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
