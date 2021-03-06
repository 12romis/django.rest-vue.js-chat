from rest_framework import serializers
from chat_room.models import Room, Chat
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    """ User serializer """
    class Meta:
        model = User
        fields = ("id", "username")


class RoomSerializer(serializers.ModelSerializer):
    """ Chat room serializer """
    creator = UserSerializer()
    invited = UserSerializer(many=True)
    date = serializers.DateTimeField(format="%H:%M:%S %d-%m-%Y")

    class Meta:
        model = Room
        fields = ("id", "creator", "invited", "date")


class ChatSerializer(serializers.ModelSerializer):
    """ Chat serializer """
    user = UserSerializer()
    date = serializers.DateTimeField(format="%H:%M:%S %d-%m-%Y")

    class Meta:
        model = Chat
        fields = ("user", "text", "date")


class ChatPostSerializer(serializers.ModelSerializer):
    """ Creating new msg serializer """

    class Meta:
        model = Chat
        fields = ("text", "room")
