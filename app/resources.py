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

    type = Field(
        column_name='type',
        attribute='type',
        widget=ForeignKeyWidget(model=BikeType, field='name')
    )

    def dehydrate_is_available(self, bike):
        return "Да" if bike.is_available else "Нет"

    def get_export_headers(self):
        styled_headers = {
            'brand': 'Бренд',
            'type': 'Тип велосипеда',
            'id': 'ID',
            'name': 'Название',
            'color': 'Цвет',
            'frame_size_inches': 'Размер рамы (в дюймах)',
            'cost_per_hour': 'Стоимость аренды (в час)',
            'is_available': 'Доступен'
        }

        headers = super().get_export_headers()
        for i, h in enumerate(headers):
            headers[i] = styled_headers[h]

        return headers

    class Meta:
        model = Bike
        export_order = (
            'id', 'name', 'brand', 'type', 'color', 'frame_size_inches', 'cost_per_hour', 'is_available'
        )


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

    type = Field(
        column_name='type',
        attribute='type',
        widget=ForeignKeyWidget(model=CarType, field='name')
    )

    def dehydrate_is_available(self, bike):
        return "Да" if bike.is_available else "Нет"

    def get_export_headers(self):
        styled_headers = {
            'id': 'ID',
            'name': 'Название',
            'brand': 'Бренд',
            'type': 'Тип',
            'required_category': 'Водительская категория',
            'horse_powers': 'Лошадиные силы',
            'zero_to_hundred_seconds': '0-100 (в секундах)',
            'trunk_capacity_liters': 'Ёмкость багажника (в литрах)',
            'seats_amount': 'Количество мест',
            'years_in_use': 'Лет в эксплуатации',
            'mileage_km': 'Километраж',
            'cost_per_hour': 'Стоимость аренды (в час)',
            'is_available': 'Доступен'
        }

        headers = super().get_export_headers()
        for i, h in enumerate(headers):
            headers[i] = styled_headers[h]

        return headers

    class Meta:
        model = Car
        export_order = (
            'id', 'name', 'brand', 'type', 'required_category', 'horse_powers', 'zero_to_hundred_seconds',
            'trunk_capacity_liters', 'seats_amount', 'years_in_use', 'mileage_km', 'cost_per_hour',
            'is_available'
        )


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
