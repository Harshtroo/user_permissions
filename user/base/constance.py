from enum import Enum


class Role(Enum):
    Admin = 'Admin'
    Supervisor = 'Supervisor'
    Manager = 'Manager'


    @classmethod
    def choices(cls):
        return tuple((role.name, role.value) for role in cls)    
    