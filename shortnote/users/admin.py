from django.contrib import admin
from shortnote.users.models import User, Role

admin.site.register(User)
admin.site.register(Role)
