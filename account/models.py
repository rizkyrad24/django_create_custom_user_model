from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
# Create your models here.

class UserCustom(AbstractUser):
    email = models.EmailField(_("email address"), unique=True)
    phone = models.CharField(_("phone number"), unique=True, max_length=15)
    REQUIRED_FIELDS = ["email", "phone"]
    
    class Meta(AbstractUser.Meta):
        swappable = "AUTH_USER_MODEL"