from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.functions import Lower
import os
from .storage import OverwriteStorage


def image_name(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (instance.username, ext)
    return os.path.join('users', filename)


class User(AbstractUser):
    USER_TYPE_CHOICES = (
        (1, 'Student'),
        (2, 'Teacher'),
    )

    email = models.EmailField(unique=True)
    user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES, default=1)
    image = models.ImageField(null=True, blank=True, upload_to=image_name)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        constraints = [
            models.UniqueConstraint(
                Lower('first_name'),
                Lower('last_name').desc(),
                name='first_last_name_unique',
            ),
        ]
