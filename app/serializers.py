from rest_framework import serializers

from .models import *


class BikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bike
        fields = [
            "id",
            "name",
            "color",
            "brand",
            "type",
            "frame_size_inches",
            "cost_per_hour",
            "is_available"
        ]


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = [
            "id",
            "name",
            "mileage_km",
            "years_in_use",
            "required_category",
            "horse_powers",
            "zero_to_hundred_seconds",
            "trunk_capacity_liters",
            "seats_amount",
            "type",
            "cost_per_hour",
            "is_available"
        ]


class BikeTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BikeType
        fields = [
            "name",
            "material",
            "tire_width",
            "segment"
        ]


class CarTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CarType
        fields = [
            "name",
            "body_type",
            "engine_type",
            "segment"
        ]


class BrandSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Brand
        fields = [
            "name",
            "country"
        ]


class Segment(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Segment
        fields = [
            "name",
            "user_type"
        ]
