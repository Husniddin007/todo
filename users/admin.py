from django.contrib import admin

from .models import UserAuth, User

admin.site.register(UserAuth)
admin.site.register(User)
