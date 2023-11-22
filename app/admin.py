import simple_history
from django.contrib import admin
from django.contrib.auth.models import User

from .models import *


admin.site.register(Bike)
admin.site.register(BikeType)
admin.site.register(Car)
admin.site.register(CarType)
admin.site.register(Brand)
admin.site.register(Segment)

simple_history.register(User)
