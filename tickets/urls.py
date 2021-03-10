from django.urls import path, include
from rest_framework import routers
from .views.TicketsViewSet import TicketsViewSet

app_name = 'tickets'

ROUTER = routers.SimpleRouter()
ROUTER.register('tickets', TicketsViewSet, basename='tickets')

urlpatterns = [
    path('', include(ROUTER.urls)),
]
