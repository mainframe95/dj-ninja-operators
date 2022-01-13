from datetime import datetime
from ninja import Schema
from typing import List


class CountryListSchema(Schema):
    id: int
    name: str
    isActive: bool
    createdAt: datetime

class CountrySchema(Schema):
    name: str

class searchSchema(Schema):
    ids: List[int]