from django.contrib import admin

from .models import Meeting, Choice, Room, Mdate

admin.site.register(Meeting)
admin.site.register(Choice)
admin.site.register(Room)
admin.site.register(Mdate)