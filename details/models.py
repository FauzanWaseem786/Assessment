from django.db import models

# Create your models here.
class Country(models.Model):
    id = models.AutoField(primary_key=True)
    Name=models.CharField(max_length=26)
    Description=models.TextField(max_length=248)
    Population=models.IntegerField()
    GDP=models.FloatField()
    # creatin dictionary of cities in states  using @property-------------
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
    # creatin dictionary of cities in states  using @property------------------
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
    City=models.ForeignKey(City, on_delete=models.CASCADE,blank=True)
    Town=models.ForeignKey(Town, on_delete=models.CASCADE,blank=True)
