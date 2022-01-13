from datetime import datetime
from ninja import Schema

class CountryListSchema(Schema):
    id: int
    name: str
    isActive: bool
    createdAt: datetime

class CountrySchema(Schema):
    name: str