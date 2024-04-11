from typing import Iterable
from django.db import models
from django.contrib.auth.models import AbstractUser
from apps.shared.models import AbstractBaseModel
from phonenumber_field.modelfields import PhoneNumberField


class UserAvatars(AbstractBaseModel):
    avatar = models.ImageField(upload_to = 'users/avatars/', default = 'users/avatars/avatar.jpeg')

    def __str__(self) -> str:
        return self.avatar.url


class UserProfile(AbstractBaseModel):
    avatar = models.ForeignKey("users.UserAvatars", models.CASCADE, related_name = "user_profiles", blank = True,
                               null = True)
    bio = models.CharField(max_length = 44, blank = True, null = True)
    first_name = models.CharField(max_length = 60, blank = True, null = True)
    last_name = models.CharField(max_length = 60, blank = True, null = True)
    phone_number = PhoneNumberField(region = "UZ")
    username = models.CharField(max_length = 150)
    birthday = models.DateField(blank = True, null = True)
    user = models.OneToOneField("users.User", on_delete = models.DO_NOTHING, related_name = "accounts", null = True,
                                blank = True)

    posts = models.ForeignKey("users.Post", models.CASCADE, related_name = "user_profiles", blank = True, null = True)
    accounts = models.ForeignKey("chat.Account", models.CASCADE, related_name = "user_profiles")

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"


class User(AbstractUser):
    phone_number = PhoneNumberField(region = 'UZ')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Post(AbstractBaseModel):
    video = models.FileField(upload_to = "users/posts/")
    descriptions = models.CharField(max_length = 180, blank = True, null = True)

    def __str__(self) -> str:
        return self.video.url


__all__ = ("UserAvatars", "UserProfile", "User", "Post")
