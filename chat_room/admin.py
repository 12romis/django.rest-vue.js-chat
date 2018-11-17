from django.contrib import admin
from chat_room.models import Room, Chat


class RoomAdmin(admin.ModelAdmin):
    """ Chat rooms """
    list_display = ('creator', 'invited_users', 'date')

    def invited_users(self, obj):
        return "\n".join([user.username for user in obj.invited.all()])


class ChatAdmin(admin.ModelAdmin):
    """ Chat admin"""
    list_display = ('room', 'user', 'text', 'date')


admin.site.register(Chat, ChatAdmin)
admin.site.register(Room, RoomAdmin)
