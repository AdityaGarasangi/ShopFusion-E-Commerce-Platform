from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)
    email = models.EmailField(max_length=254)
    image = models.ImageField(
        default="user_uploads/default-pfp.jpg",
        upload_to="user_uploads",
        blank=True,
    )

    def __str__(self):
        return self.user.username
