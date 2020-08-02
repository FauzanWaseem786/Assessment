from django.contrib import admin
from details.models import Country,State,City,Town,Person
# Register your models here.
admin.site.register(Country)
admin.site.register(State)
admin.site.register(City)
admin.site.register(Town)
admin.site.register(Person)
