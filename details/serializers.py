from rest_framework import serializers
from details.models import Country,State,City,Town,Person
# serializers for all models-------------------
class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields=('__all__')
class StateSerializer(serializers.ModelSerializer):
    cities=CitySerializer(many=True)
    class Meta:
        model = State
        fields=(
            "id",
            "Name",
            "Description",
            "Population",
            "GDP",
            "cities"
        )
#-----------------# Nested srilaizers fro Country CRUD  -------------------------
    def create(self,data):
        cities=data.pop('cities')
        state=State.objects.create(**data)
        for city in cities:
            City.objects.create(**city,State=state)
        return state

class CountrySerializer(serializers.ModelSerializer):
    states=StateSerializer(many=True)
    state_list=serializers.SerializerMethodField('get_states')#list of states using SerializerMethodField
    city_list=serializers.SerializerMethodField('get_cities')#list of cities using SerializerMethodField
    class Meta:
        model = Country
        fields=(
            "id",
            "Name",
            "Description",
            "Population",
            "GDP",
            "states",#dictionary of states  having cities in a country
            "state_list",
            "city_list"
        )
#----------------- Nested srilaizers fro Country CRUD  -------------------------
    def create(self,data):
        states=data.pop('states')
        country=Country.objects.create(**data)
        for state in states:
            State.objects.create(**state,Country=country)
        return country
#------------------list of states in a country-----------------------------------------------
    def get_states(self,country):
        a=[]
        for state in State.objects.all():
            if(state.Country.Name==country.Name):
                a.append(state.Name)
        return a
#------------------list of cities in a country-----------------------------------------------
    def get_cities(self,country):
        a=[]
        for city in City.objects.all():
            if(city.Country.Name==country.Name):
                a.append(city.Name)
        return a

class TownSerializer(serializers.ModelSerializer):
    class Meta:
        model = Town
        fields=('__all__')
class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields=('__all__')
