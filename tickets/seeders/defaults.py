from django.contrib.auth import get_user_model
from django.contrib.auth.models import Permission
from tickets.models import Tickets
from faker import Faker

faker = Faker('es_ES')

User = get_user_model()

# creeate superuser
superuser = User.objects.create(
    username='superuser',
    first_name=faker.first_name(),
    last_name=faker.last_name(),
    is_staff=True,
    is_superuser=True,
)
superuser.set_password(12345678)
superuser.save()

# creeate viewuser
viewuser = User.objects.create(
    username='viewuser',
    first_name=faker.first_name(),
    last_name=faker.last_name(),
)
viewuser.set_password(12345678)
viewuser.save()

# creeate viewcreateuser
viewcreateuser = User.objects.create(
    username='viewcreateuser',
    first_name=faker.first_name(),
    last_name=faker.last_name(),
)
viewcreateuser.set_password(12345678)
viewcreateuser.save()
addPerm = Permission.objects.get(codename='add_tickets')
viewcreateuser.user_permissions.add(addPerm)

# tickets
for el in range(30):
    Tickets.objects.create(title=faker.sentence(), status='open', author=viewcreateuser, description=faker.paragraph(nb_sentences=10))
