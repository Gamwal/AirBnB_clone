#!/usr/bin/python3
from uuid import uuid4
from datetime import datetime

class BaseModel():

    def __init__(self, my_number=None, name=None, id=None, created_at=None, updated_at=None):

        self.name = name
        self.my_number = my_number

        if id == None:
            self.id = uuid4().__str__()

        if created_at == None:
            self.created_at = datetime.today()

        if updated_at == None:
            self.updated_at = datetime.today()

    def save(self):
        self.updated_at = datetime.today()

    def __str__(self):
        new_dict = self.__dict__()
        del new_dict["__class__"]
        to_print = f"[{self.__class__.__name__}] ({self.id}) {new_dict}"
        return to_print

    def __dict__(self):
        return {"my_number":self.my_number, "name":self.name,
                "__class__":self.__class__.__name__, "updated_at":self.updated_at,
                "id":self.id, "created_at":self.created_at}

    def to_dict(self):
        loc_dict = self.__dict__()
        loc_dict["created_at"] = self.created_at.isoformat()
        loc_dict["updated_at"] = self.updated_at.isoformat()
        return(loc_dict)
