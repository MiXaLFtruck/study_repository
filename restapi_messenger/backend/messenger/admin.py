from django.contrib import admin
from .models import AppUser, Room, Message

admin.site.register(AppUser)
admin.site.register(Room)
admin.site.register(Message)
