from django_filters import rest_framework as filters
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from ..models import Tickets
from ..serializers.TicketsSerializer import TicketsSerializer


class TicketsViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated, DjangoModelPermissions, )
    serializer_class = TicketsSerializer
    queryset = Tickets.objects.all()
    filter_backends = (filters.DjangoFilterBackend, OrderingFilter,)

    def create(self, request):
        data = request.data
        data['author'] = request.user.pk
        ser = self.get_serializer(data=data)
        ser.is_valid(raise_exception=True)
        ser.save()
        return Response(ser.data, status=status.HTTP_201_CREATED)
