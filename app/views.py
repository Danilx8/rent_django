from django.db.models import Q
from django.http import JsonResponse
from rest_framework import generics  # Готовые представления для наследования
from rest_framework.permissions import AllowAny  # Импорт прав доступа к представлению
from rest_framework import viewsets
from rest_framework.response import Response

from .models import *
from .serializers import *


class BikeViewSet(viewsets.ModelViewSet):
    queryset = Bike.objects.all()
    serializer_class = BikeSerializer


class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer


class BikesByType(generics.ListAPIView):
    def get(self, request, *args, **kwargs):
        queryset = Bike.objects.filter(
            type_id=kwargs.get("passed_type")
        )
        serializer_class = BikeSerializer(queryset, many=True)

        return JsonResponse(serializer_class.data, safe=False)


class CarsByCategoryApiView(generics.ListAPIView):
    def get(self, request, *args, **kwargs):
        queryset = Car.objects.filter(
            Q(required_category=kwargs.get("passed_category"))
        )
        serializer_class = CarSerializer(queryset, many=True)

        return JsonResponse(serializer_class.data, safe=False)
