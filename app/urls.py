from django.urls import path, include, re_path
from rest_framework import routers

from app.views import *

router = routers.DefaultRouter()
router.register(r'bikes', BikeViewSet)
router.register(r'cars', CarViewSet)

urlpatterns = [
    path('', include(router.urls)),
    re_path(r'cars/(?P<passed_category>[A-E])', CarsByCategoryApiView.as_view()),
    re_path(r'bikes/(?P<passed_type>\w)', BikesByType.as_view()),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
