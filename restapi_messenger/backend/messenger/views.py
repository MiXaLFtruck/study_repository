from django.shortcuts import render
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import *
from .models import *


# class UserViewset(viewsets.ModelViewSet):
#     queryset = AppUser.objects.all()
#     serializer_class = UserSerializer


# class RoomViewset(viewsets.ModelViewSet):
#     queryset = Room.objects.all()
#     serializer_class = RoomSerializer
#
#
# class MessageViewest(viewsets.ModelViewSet):
#     queryset = Message.objects.all()
#     serializer_class = MessageSerializer


class UserAPIListView(generics.ListCreateAPIView):
    """
    По url api/users представление выдает список всех пользователей (по GET-запросу)
    и/или позволяет добавить пользователя (по POST-запросу)
    По url api/rooms/<room_id>/users представление выдает список всех пользователей
    в конкретной комнате (по GET-запросу)
    """
    # queryset = AppUser.objects.all()
    serializer_class = UserSerializer

    def get_queryset(self):
        if self.kwargs:
            return AppUser.objects.filter(room__id=self.kwargs['pk'])
        else:
            return AppUser.objects.all()


class UserAPIRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
    Представление выдает конкретного пользователя (по GET-запросу), редактирует его (по PUT- или PATCH-запросу)
    и/или удаляет (по DELETE-запросу)
    """
    queryset = AppUser.objects.all()
    serializer_class = UserSerializer


class RoomAPIListView(generics.ListCreateAPIView):
    """
    По url api/rooms представление выдает список всех "комнат" (по GET-запросу)
    и/или позволяет добавить новую "комнату" (по POST-запросу)
    По url api/users/<user_id>/rooms представление выдает список всех "комнат",
    в которых участвует конкретный пользователь (по GET-запросу)
    """
    # queryset = Room.objects.all()
    serializer_class = RoomSerializer

    def get_queryset(self):
        if self.kwargs:
            return Room.objects.filter(users__id=self.kwargs['pk'])
        else:
            return Room.objects.all()


class RoomAPIRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
    Представление выдает конкретную "комнату" (по GET-запросу), редактирует ее (по PUT- или PATCH-запросу)
    и/или удаляет ее (по DELETE-запросу)
    """
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class MessageAPIListView(generics.ListAPIView):
    """
    Представление выдает все сообщения в конкретной комнате (по GET-запросу)
    """
    serializer_class = MessageSerializer

    def get_queryset(self):
        return Message.objects.filter(to_room_id=self.kwargs['pk'])


# class RoomAPIListView(APIView):
#
#     def get(self, request):
#         rooms = Room.objects.all()
#         json = RoomSerializer(rooms, many=True, context={'request': request}).data
#         return Response({'rooms': json})
#
#     def post(self, request):
#         serializer = RoomSerializer(data=request.data, context={'request': request})
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({'room': serializer.data})


@api_view(['POST'])
def upload_image(request):
    data = request.data

    obj_id = data['id']
    obj = AppUser.objects.get(id=obj_id)

    obj.avatar = request.FILES.get('avatar')
    obj.save()

    return Response('Image was uploaded')