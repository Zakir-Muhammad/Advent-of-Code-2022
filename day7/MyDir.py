from __future__ import annotations
from typing import Union
from MyFile import *

class Directory:
    """
    A node
    """

    #Attribute Types
    # sub: list[Union[Directory, File]]
    # size: int
    # name: str
    # parent: Directory

    def __init__(self, parent: Directory, name: str):
        self.sub = []
        self.size = 0
        self.name = name
        self.parent = parent

    def get_size(self) -> int:
        s = 0
        for child in self.sub: s += child.get_size()
        return s

    def get_name(self):
        return self.name

    def add_child(self, child: Union[Directory, File]):
        self.sub.append(child)
        self.size = child.get_size()

    def is_root(self):
        return not self.parent

    # Given a directory and a name of a child, returns the child
    def change(self, item_name: str) -> Union[Directory, File]:
        for child in self.sub:
            if item_name == child.name: return child

    def __contains__(self, item_name: str) -> bool:
        for child in self.sub:
            if item_name == child.name: return True
        return False

    def __str__(self) -> str:
        s = ""
        for item in self.sub:
            if isinstance(item, Directory): s += item.name + "\n"
            s += item.__str__()
        return s
