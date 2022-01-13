from datetime import datetime
from ninja import Schema

class UserListSchema(Schema):
    id: int
    name: str
    email: str
    isActive: bool
    date_joined: datetime


class UserSchema(Schema):
    name: str
    email: str
    password: str
    isActive: bool

class UserUpateSchema(Schema):
    name: str
    email: str
