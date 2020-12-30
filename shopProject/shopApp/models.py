from django.db import models
from django.contrib.auth.models import User

class UserBasicInfoModels(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    portfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='users_profile_pictures', blank=True)

    def __str__(self):
        return self.user.username


