from __future__ import annotations
from MyDir import *


class File:
    """
    A file
    """

    #Attribute Types
    # size: int
    # name: str
    # parent: Directory

    def __init__(self, parent, name, size):
        self.parent = parent
        self.size = size
        self.name = name

    def get_size(self) -> int:
        return self.size

    def get_name(self):
        return self.name

    def __str__(self):
        return self.name + "\n"
