
from enum import Enum


class Role(Enum):
    SUPERADMIN = 1
    ADMIN = 2
    CONSULTANT = 3

    def __lt__ (self, other):
        if self.__class__ is other.__class__:
            return self.value < other.value

    def __str__(self) -> str:
        return self.name

    
        