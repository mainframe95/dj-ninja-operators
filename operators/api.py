from os import name
from typing import List
from ninja import NinjaAPI
from core.common.schema import NotFoundSchema
from .schema import OperatorListSchema, OperatorSchema, OperatorUpdatedSchema
from .models import Operator

from users.models import User
from countries.models import Country


api = NinjaAPI(urls_namespace='operators')

@api.get("/list", response={200: List[OperatorListSchema]|OperatorListSchema, 404: NotFoundSchema})
def listOperator(request, operatorId: int=None ):
    if operatorId:
        try:
            return Operator.objects.get(pk = operatorId)
        except Operator.DoesNotExist as e:
            return 404, {"message": "Operator does not exist"}
    operator = Operator.objects.all()
    return 200, operator

@api.post("/create", response= {201: OperatorListSchema, 404: NotFoundSchema})
def createOperator(request, data: OperatorSchema):
    try:
        data.createdBy = User.objects.get(pk = data.createdBy)
    except User.DoesNotExist as e:
        return 404, {"message": " User does not exist"}
    try:
        data.country = Country.objects.get(pk = data.country)
    except Country.DoesNotExist as e:
        return 404, {"message": " Country does not exist"}
    try:
        operator = Operator.objects.create(**data.dict())
        return 201, operator
    # partie a voir
    except Operator.unique_error_message as e:
        return 404, {"message": " Operator already exist"}
    


@api.put("/update/{operatorId}", response= {200: OperatorListSchema, 404: NotFoundSchema})
def operatorUpdated(request, operatorId: int, data: OperatorUpdatedSchema):
    try:
        operator = Operator.objects.get(pk = operatorId)
        for attribute, value in data.dict().items():
            if not data.name ==  None:
                setattr(operator, attribute, value)
        operator.save()
        return 200, operator
    except Operator.DoesNotExist as e:
        return 404, {"message": " Operator does not exist"}

