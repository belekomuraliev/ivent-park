
from PIL import Image
from io import BytesIO
from django.core.files import File
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class IventUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    register = models.DateField(auto_now_add=True)



    def __str__(self):
        return self.user.username


