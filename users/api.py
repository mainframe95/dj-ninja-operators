from os import name
from typing import List
from ninja import NinjaAPI
from core.common.schema import NotFoundSchema

from users.schema import UserListSchema, UserSchema, UserUpateSchema
from .models import User


api = NinjaAPI()


@api.get("/")
def hello(request):
    return "Hello world"

@api.get("/list", response={200: List[UserListSchema]|UserListSchema, 404: NotFoundSchema})
def listUser(request, userId: int=None ):
    if userId:
        try:
            return User.objects.get(pk = userId)
        except User.DoesNotExist as e:
            return 404, {"message": "User does not exist"}
    users = User.objects.all()
    return users

@api.post("/register", response= {201: UserListSchema})
def userRegister(request, data: UserSchema):
    register = User.objects.create(**data.dict())
    return 201, register

@api.put("/update/{userId}", response= {200: UserListSchema, 404: NotFoundSchema})
def userUpdated(request, userId: int, data: UserUpateSchema):
    try:
        user = User.objects.get(pk = userId)
        # user(name = data.name, email = data.email)
        for attribute, value in data.dict().items():
            setattr(user, attribute, value)
        user.save()
        return 200, user
    except User.DoesNotExist as e:
        return 404, {"message": " User does not exist"}

