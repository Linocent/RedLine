from django.db import models
from django.contrib.auth.models import User


class Discord(models.Model):
    discord_id = models.CharField(max_length=50, primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.discord_id, self.user}"
