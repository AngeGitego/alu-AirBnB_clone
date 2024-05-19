<<<<<<< HEAD
#!/usr/bin/python3
"""This module creates a User class"""

from models.base_model import BaseModel


class City(BaseModel):
    """Class for managing city objects"""

    state_id = ""
    name = ""
=======
#!/usr/bin/python3
"""
Module for the City class.
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    Represent a city.

    Attributes:
        state_id (str): The state id.
        name (str): The name of the city.
    """

    state_id = ""
    name = ""
>>>>>>> 9c15d210529583cfd1fbcd5823cd2006914994c8
