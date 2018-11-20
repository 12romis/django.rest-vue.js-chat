from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions

from chat_room.models import Room, Chat
from chat_room.serializers import RoomSerializer, ChatSerializer, ChatPostSerializer


class Rooms(APIView):
    """ Char room """
    def get(self, request):
        rooms = Room.objects.all()

        serializer = RoomSerializer(rooms, many=True)
        return Response({"data": serializer.data})


class Dialog(APIView):
    """ Dialog """
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        room_id = request.GET.get('room')
        chat = Chat.objects.filter(room_id=room_id)
        serializer = ChatSerializer(chat, many=True)
        return Response({"data": serializer.data})

    def post(self, request):
        dialog = ChatPostSerializer(data=request.data)
        if dialog.is_valid():
            dialog.save(user=request.user)
            return Response(status=201)
        else:
            return Response({"errors": dialog.errors}, status=400)

