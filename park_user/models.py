from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    register = models.DateField(auto_now_add=True)
    email = models.EmailField(max_length=30)
    point = models.IntegerField(default=0)


    def __str__(self):
        return self.user.username


