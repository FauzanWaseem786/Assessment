from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from details.models import Country,State,City,Town,Person
from details.serializers import CountrySerializer,StateSerializer,CitySerializer,TownSerializer,PersonSerializer
# Create your views here.
## CRUD For Country---------------------------------------------------
@api_view(['GET', 'POST'])
def country_create(request):
    if request.method == 'GET':
        countries = Country.objects.all()
        serializer = CountrySerializer(countries, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = request.data
        serializer = CountrySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
@api_view(['POST'])
def country_retrieve(request, pk):
    country = Country.objects.get(id=pk)
    serializer = CountrySerializer(country, many=False)
    return Response(serializer.data)
@api_view(['PUT'])
def country_update(request, pk):
    country = Country.objects.get(id=pk)
    serializer = CountrySerializer(instance=country, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
@api_view(['DELETE'])
def country_delete(request, pk):
    country = Country.objects.get(id=pk)
    country.delete()

    return Response("Country Deleted")

## CRUD For State---------------------------------------------------
@api_view(['GET', 'POST'])
def state_create(request):
    if request.method == 'GET':
        states = State.objects.all()
        serializer = StateSerializer(states, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = request.data
        serializer = StateSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
@api_view(['POST'])
def state_retrieve(request, pk):
    state = State.objects.get(id=pk)
    serializer = CountrySerializer(state, many=False)
    return Response(serializer.data)
@api_view(['PUT'])
def state_update(request, pk):
    state = State.objects.get(id=pk)
    serializer = StateSerializer(instance=state, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
@api_view(['DELETE'])
def state_delete(request, pk):
    state = State.objects.get(id=pk)
    state.delete()
    return Response("State Deleted")

## CRUD For City---------------------------------------------------
@api_view(['GET', 'POST'])
def city_create(request):
    if request.method == 'GET':
        cities = City.objects.all()
        serializer = CitySerializer(cities, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = request.data
        serializer = CitySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
@api_view(['POST'])
def city_retrieve(request, pk):
    city = City.objects.get(id=pk)
    serializer = CitySerializer(city, many=False)
    return Response(serializer.data)
@api_view(['PUT'])
def city_update(request, pk):
    city = City.objects.get(id=pk)
    serializer = CitySerializer(instance=city, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
@api_view(['DELETE'])
def city_delete(request, pk):
    city = City.objects.get(id=pk)
    city.delete()
    serializer = CitySerializer(city, many=False)
    return Response("City Deleted")

## CRUD For Town---------------------------------------------------
@api_view(['GET', 'POST'])
def town_create(request):
    if request.method == 'GET':
        towns = Town.objects.all()
        serializer = TownSerializer(towns, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = request.data
        serializer = TownSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
@api_view(['POST'])
def town_retrieve(request, pk):
    town = Town.objects.get(id=pk)
    serializer = TownSerializer(town, many=False)
    return Response(serializer.data)
@api_view(['PUT'])
def town_update(request, pk):
    town = Town.objects.get(id=pk)
    serializer = TownSerializer(instance=town, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
@api_view(['DELETE'])
def town_delete(request, pk):
    town = Town.objects.get(id=pk)
    town.delete()
    return Response("City Deleted")

## CRUD For Person---------------------------------------------------
@api_view(['GET','POST'])
def person_create(request):
    if request.method == 'GET':
        persons = Town.objects.all()
        serializer = PersonSerializer(persons, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = request.data
        serializer = PersonSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data )
        return Response(serializer.errors)
@api_view(['POST'])
def person_retrieve(request, pk):
    person = Person.objects.get(id=pk)
    serializer = PersonSerializer(person, many=False)
    return Response(serializer.data)
@api_view(['PUT'])
def person_update(request, pk):
    person = Person.objects.get(id=pk)
    serializer = PersonSerializer(instance=person, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
@api_view(['DELETE'])
def person_delete(request, pk):
    person = Person.objects.get(id=pk)
    person.delete()
    return Response("Person Deleted")

# END of CRUDs--------------------------------------------------------------
