from ninja import Schema
from pydantic.types import NonPositiveFloat
from countries.schema import CountryListSchema
from users.schema import UserListSchema

class OperatorSchema(Schema):
    name: str
    clients: int
    country: int
    createdBy: int

class OperatorUpdatedSchema(Schema):
    name: str = None
    clients: int = None
    # country: int



class OperatorListSchema(Schema):
    id: int
    name: str
    clients: int
    country: CountryListSchema
    createdBy: UserListSchema