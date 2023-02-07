#!/usr/bin/python3

class BaseModel(cmd.Cmd):

    def __init__(self, id=None, created_at=None, updated_at=None):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime()
        self.updated_at = datetime.datetime()

    @property
    def id(self):
        pass

    @id.setter
    def id(self):
        pass

    def __str__(self):
        pass

    def __dict__(self):
        pass

    def save(self):
        pass

    def to_dict(self):


