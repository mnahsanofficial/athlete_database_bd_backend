from django.contrib.auth.models import User
from django.db import models

class Federation(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    contact_number = models.CharField(max_length=15)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="created_federations")
    is_approved = models.BooleanField(default=False)

class PlayerProfile(models.Model):
    federation = models.ForeignKey(Federation, on_delete=models.CASCADE, related_name="players")
    name = models.CharField(max_length=100)
    sport = models.CharField(max_length=50)
    achievements = models.TextField()
    records = models.TextField()
    history = models.TextField()
    approved = models.BooleanField(default=False)
