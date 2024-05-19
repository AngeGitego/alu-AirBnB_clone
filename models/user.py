<<<<<<< HEAD
#!/usr/bin/python3
"""This module creates a User class"""
from models.base_model import BaseModel


class User(BaseModel):
    """Class for managing user objects"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
=======
#!/usr/bin/python3
"""
Module for the User class.
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    class User that handles users' information
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
>>>>>>> 9c15d210529583cfd1fbcd5823cd2006914994c8
