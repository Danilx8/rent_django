import simple_history
from django.contrib import admin
from django.contrib.auth.models import User
from django.utils.html import format_html
from import_export.admin import ExportActionModelAdmin

from .resources import *


class BikeAdmin(ExportActionModelAdmin):
    readonly_fields = ('id',)
    list_display = ('name', 'show_brand', 'show_type', 'show_segment', 'is_available')
    list_filter = ('is_available', 'brand', 'type',)
    resource_class = BikeResource

    def show_type(self, obj):
        result = BikeType.objects.get(pk=obj.type.id)
        url = "http://localhost:8000/bikes/" + str(obj.type.id)
        return format_html('<a href="{}">{}</a>', url, result)

    def show_segment(self, obj):
        type = BikeType.objects.get(pk=obj.type.id)
        segment = Segment.objects.get(pk=type.segment.id)
        return segment

    def show_brand(self, obj):
        brand = Brand.objects.get(pk=obj.brand.id)
        return brand


class BikeTypeAdmin(ExportActionModelAdmin):
    resource_class = BikeTypeResource


class CarAdmin(ExportActionModelAdmin):
    readonly_fields = ('id',)
    list_display = ('name', 'show_brand', 'show_type', 'show_segment', 'is_available')
    list_filter = ('is_available', 'brand', 'type',)
    search_fields = ("name__startswith",)
    resource_class = CarResource

    def show_type(self, obj):
        result = CarType.objects.get(pk=obj.type.id)
        return result

    def show_segment(self, obj):
        type = self.show_type(obj)
        segment = Segment.objects.get(pk=type.segment.id)
        return segment

    def show_brand(self, obj):
        brand = Brand.objects.get(pk=obj.brand.id)
        return brand


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
