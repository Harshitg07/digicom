from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from groups.models import Group
from django.urls import reverse

# Create your models here.
current_user = get_user_model()


class Post(models.Model):

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='user', default=current_user)
    created_at = models.DateTimeField(auto_now=True)
    message = models.TextField()
    group = models.ForeignKey(
        Group, on_delete=models.CASCADE, null=True, blank=True, related_name='posts')

    def __str__(self):
        return self.message

    def get_absolute_url(self):
        return reverse('posts:list')
