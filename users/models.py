from django.contrib.auth.models import AbstractUser
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

class CustomUser(AbstractUser):
    profile_picture = ProcessedImageField(
        default='default-user.png', processors=[ResizeToFill(30, 30)], format='PNG')
