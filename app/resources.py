from import_export import resources
from import_export.fields import Field
from import_export.widgets import ForeignKeyWidget

from .models import *


class BikeResource(resources.ModelResource):
    brand = Field(
        column_name='brand',
        attribute='brand',
        widget=ForeignKeyWidget(model=Brand, field='name')
    )

    class Meta:
        model = Bike


class BikeTypeResource(resources.ModelResource):
    segment = Field(
        column_name='segment',
        attribute='segment',
        widget=ForeignKeyWidget(model=Segment, field='name')
    )

    class Meta:
        model = BikeType


class CarResource(resources.ModelResource):
    brand = Field(
        column_name='brand',
        attribute='brand',
        widget=ForeignKeyWidget(model=Brand, field='name')
    )

    class Meta:
        model = Car


class CarTypeResource(resources.ModelResource):
    segment = Field(
        column_name='segment',
        attribute='segment',
        widget=ForeignKeyWidget(model=Segment, field='name')
    )

    class Meta:
        model = CarType


class BrandResource(resources.ModelResource):
    class Meta:
        model = Brand


class SegmentResource(resources.ModelResource):
    class Meta:
        model = Segment
