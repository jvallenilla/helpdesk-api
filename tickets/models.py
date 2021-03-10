from django.db import models
from django.contrib import admin
from django.contrib.auth import get_user_model

User = get_user_model()


class Tickets(models.Model):
    STATUSES = (
        ('open', 'Abierto'),
        ('pending', 'Pendiente'),
        ('in_process', 'En Proceso'),
        ('resolved', 'Resuelto'),
        ('closed', 'Cerrado'),
    )

    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(max_length=50, choices=STATUSES, default='open')
    author = models.ForeignKey(
        User,
        related_name='user_tickets',
        on_delete=models.CASCADE
    )

    class Meta:
        db_table = 'tickets__tickets'

    def __str__(self):
        return "{}_{}...".format(self.id, self.title[:10])


@admin.register(Tickets)
class TicketsAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_at', 'title', 'get_short_desc', 'status',)
    list_filter = ('created_at', 'status', 'author__username')
    search_fields = ('title', 'description')

    def get_short_desc(self, instance):
        return "{}...".format(instance.description[:80]) if len(instance.description) > 80 else instance.description
