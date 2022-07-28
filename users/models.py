from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.functions import Lower
from utils.helping_functions import get_user_image_name


class User(AbstractUser):
    USER_TYPE_CHOICES = (
        (1, 'Student'),
        (2, 'Teacher'),
    )

    email = models.EmailField(unique=True)
    user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES, default=1)
    image = models.ImageField(null=True, upload_to=get_user_image_name)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def user_type_str(self):
        if self.user_type == 1:
            return 'Student'
        return 'Teacher'

    class Meta:
        constraints = [
            models.UniqueConstraint(
                Lower('first_name'),
                Lower('last_name').desc(),
                name='first_last_name_unique',
            ),
        ]
