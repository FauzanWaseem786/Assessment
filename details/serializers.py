from rest_framework import serializers
from details.models import Country,State,City,Town,Person
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


class CountrySerializer(serializers.ModelSerializer):
    states=StateSerializer(many=True)
    class Meta:
        model = Country
        fields=(
            "id",
            "Name",
            "Description",
            "Population",
            "GDP",
            "states"
        )



class TownSerializer(serializers.ModelSerializer):
    class Meta:
        model = Town
        fields=('__all__')
class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields=('__all__')
