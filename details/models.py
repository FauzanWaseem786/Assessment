from django.db import models

# Create your models here.
class Country(models.Model):
    id = models.AutoField(primary_key=True)
    Name=models.CharField(max_length=26)
    Description=models.TextField(max_length=248)
    Population=models.IntegerField()
    GDP=models.FloatField()
    @property
    def states(self):
        return self.state_set.all()

class State(models.Model):
    id = models.AutoField(primary_key=True)
    Name=models.CharField(max_length=26)
    Country=models.ForeignKey(Country, on_delete=models.CASCADE)
    Description=models.TextField(max_length=248)
    Population=models.IntegerField()
    GDP=models.FloatField()
    @property
    def cities(self):
        return self.city_set.all()
class City(models.Model):
    id = models.AutoField(primary_key=True)
    State=models.ForeignKey(State, on_delete=models.CASCADE)
    Country=models.ForeignKey(Country, on_delete=models.CASCADE)
    Name=models.CharField(max_length=26)
    Description=models.TextField(max_length=248)
    Population=models.IntegerField()
    GDP=models.FloatField()
    PinCode=models.CharField(max_length=6)
class Town(models.Model):
    id = models.AutoField(primary_key=True)
    State=models.ForeignKey(State, on_delete=models.CASCADE)
    Country=models.ForeignKey(Country, on_delete=models.CASCADE)
    Name=models.CharField(max_length=26)
    Description=models.TextField(max_length=248)
    Population=models.IntegerField()
    GDP=models.FloatField()
    PinCode=models.CharField(max_length=6)
class Person(models.Model):
    id = models.AutoField(primary_key=True)
    Name=models.CharField(max_length=26)
