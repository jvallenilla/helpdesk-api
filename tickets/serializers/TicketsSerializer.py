from rest_framework import serializers
from ..models import Tickets


class TicketsSerializer(serializers.ModelSerializer):
    status_display = serializers.SerializerMethodField()
    author_display = serializers.SerializerMethodField()

    class Meta:
        model = Tickets
        fields = '__all__'

    def get_status_display(self, instance):
        return instance.get_status_display()

    def get_author_display(self, instance):
        return instance.author.get_full_name()
