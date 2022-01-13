from os import name
from typing import List
from ninja import NinjaAPI
from core.common.schema import NotFoundSchema
from countries.schema import CountryListSchema, CountrySchema
from .models import Country


api = NinjaAPI(urls_namespace='countries')

@api.get("/list", response={200: List[CountryListSchema]|CountryListSchema, 404: NotFoundSchema})
def listCountry(request, countryId: int=None ):
    if countryId:
        try:
            return Country.objects.get(pk = countryId)
        except Country.DoesNotExist as e:
            return 404, {"message": "Country does not exist"}
    countries = Country.objects.all()
    return 200, countries

@api.post("/create", response= {201: CountryListSchema})
def createCountry(request, data: CountrySchema):
    country = Country.objects.create(**data.dict())
    return 201, country


@api.put("/update/{countryId}", response= {200: CountryListSchema, 404: NotFoundSchema})
def countryUpdated(request, countryId: int, data: CountrySchema):
    try:
        country = Country.objects.get(pk = countryId)
        setattr(country, name, data.name)
        country.save()
        return 200, country
    except Country.DoesNotExist as e:
        return 404, {"message": " Country does not exist"}

