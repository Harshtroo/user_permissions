from enum import Enum


class Role(Enum):
    A = 'Admin'
    S = 'Supervisor'
    M = 'Manager'


    @classmethod
    def choices(cls):
        return tuple((role.name, role.value) for role in cls)    
    