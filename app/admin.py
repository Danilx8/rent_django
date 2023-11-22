import simple_history
from django.contrib import admin
from django.contrib.auth.models import User
from import_export.admin import ExportActionModelAdmin

from .resources import *


class BikeAdmin(ExportActionModelAdmin):
    readonly_fields = ('id',)
    resource_class = BikeResource


class BikeTypeAdmin(ExportActionModelAdmin):
    resource_class = BikeTypeResource


class CarAdmin(ExportActionModelAdmin):
    readonly_fields = ('id',)
    resource_class = CarResource


class CarTypeAdmin(ExportActionModelAdmin):
    resource_class = CarTypeResource


class BrandAdmin(ExportActionModelAdmin):
    resource_class = BrandResource


class SegmentAdmin(ExportActionModelAdmin):
    resource_class = SegmentResource


admin.site.register(Bike, BikeAdmin)
admin.site.register(BikeType, BikeTypeAdmin)
admin.site.register(Car, CarAdmin)
admin.site.register(CarType, CarTypeAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(Segment, SegmentAdmin)

simple_history.register(User)
