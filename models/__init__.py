#!/usr/bin/python3
""" Initialize file for HBnB packages.
    """

from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
