from django.contrib.auth.models import User
from django.db import models


class AppUser(User):
    avatar = models.ImageField(upload_to='avatars/', default='avatars/default.png')

    class Meta:
        ordering = ['username']

    def __str__(self):
        return self.username


class Room(models.Model):
    title = models.CharField(max_length=50, unique=True)
    users = models.ManyToManyField(AppUser)
    last_message = models.DateTimeField(auto_now_add=True)
    is_direct = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Message(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    to_room = models.ForeignKey(Room, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    text = models.TextField()

    def __str__(self):
        return self.text[:50]

    def save(self):
        super().save()
        room = Room.objects.get(id=self.to_room.id)
        room.last_message = self.created
        room.save()
