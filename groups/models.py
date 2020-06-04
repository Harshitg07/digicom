from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

# Create your models here.

current_user = get_user_model()

class Group(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(blank=True)
    description = models.TextField(blank=True, null=True)
    members = models.ManyToManyField(
        User, blank=True, related_name='members', default=current_user)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("groups:detail", kwargs={"slug": self.slug})

    class Meta:
        ordering = ['-pk', ]
