from django.urls import path, include
from rest_framework import routers
from .views.TicketsViewSet import TicketsViewSet, CheckPerms

app_name = 'tickets'

ROUTER = routers.SimpleRouter()
ROUTER.register('tickets', TicketsViewSet, basename='tickets')

urlpatterns = [
    path('tickets/perms/', CheckPerms.as_view(), name='check-perms'),
    path('', include(ROUTER.urls)),
]
