from django.urls import path
from messenger.views import *

urlpatterns = [
    path('users/', UserAPIListView.as_view()),
    path('users/<int:pk>/', UserAPIRetrieveUpdateDestroyView.as_view()),
    path('users/<int:pk>/rooms/', RoomAPIListView.as_view()),
    path('rooms/', RoomAPIListView.as_view()),
    path('rooms/<int:pk>/', RoomAPIRetrieveUpdateDestroyView.as_view()),
    path('rooms/<int:pk>/users/', UserAPIListView.as_view()),
    path('rooms/<int:pk>/messages/', MessageAPIListView.as_view()),
]
