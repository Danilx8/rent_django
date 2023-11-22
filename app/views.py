from django.db.models import Q
from django.http import JsonResponse
from rest_framework import generics, status
from rest_framework.decorators import action
from rest_framework import viewsets
from rest_framework.response import Response

from .serializers import *


class BikeViewSet(viewsets.ModelViewSet):
    queryset = Bike.objects.all()
    serializer_class = BikeSerializer

    @action(detail=False, methods=["POST", ])
    def rent_bike(self, request):
        serializer = BikeSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        bike = Bike.objects.filter(pk=request.data['id'])[0]
        if not bike:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if not bike.is_available:
            return Response(data="The bike is busy", status=status.HTTP_409_CONFLICT)

        bike.is_available = False
        bike.save()
        return Response(data="bike rent successfully", status=status.HTTP_200_OK)


class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer


class BikesByType(generics.ListAPIView):
    serializer_class = BikeSerializer

    def get(self, request, *args, **kwargs):
        queryset = Bike.objects.filter(
            type_id=kwargs.get("passed_type")
        )
        serializer_class = BikeSerializer(queryset, many=True)

        return JsonResponse(serializer_class.data, safe=False)

    
class CarsByCategoryApiView(generics.ListAPIView):
    serializer_class = CarSerializer

    def get(self, request, *args, **kwargs):
        queryset = Car.objects.filter(
            Q(required_category=kwargs.get("passed_category"))
        )
        serializer_class = CarSerializer(queryset, many=True)

        return JsonResponse(serializer_class.data, safe=False)
