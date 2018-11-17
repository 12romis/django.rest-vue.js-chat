from django.db import models
from django.contrib.auth.models import User


class Room(models.Model):
    """ Model of chat room """
    creator = models.ForeignKey(User, verbose_name="Creator", on_delete=models.CASCADE)
    invited = models.ManyToManyField(User, verbose_name="Members", related_name="invited_users")
    date = models.DateTimeField('Created at', auto_now_add=True)

    class Meta:
        verbose_name = 'Chat room'
        verbose_name_plural = 'Chat rooms'


class Chat(models.Model):
    """ Model of chat """
    room = models.ForeignKey(Room, verbose_name="Chat room", on_delete=models.CASCADE)
    user = models.ForeignKey(User, verbose_name="User", on_delete=models.CASCADE)
    text = models.TextField("Message", max_length=500)
    date = models.DateTimeField("Sending date of message", auto_now_add=True)

    class Meta:
        verbose_name = "Chat message"
        verbose_name_plural = "Chat messages"

