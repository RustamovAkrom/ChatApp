from django.db import models
from apps.shared.models import AbstractBaseModel
from django.core.exceptions import ValidationError
from apps.users.models import UserProfile


class Account(AbstractBaseModel):
    chats = models.ForeignKey("chat.Chat", models.DO_NOTHING, related_name = "accounts", blank = True, null = True)
    groups = models.ForeignKey("chat.Group", models.DO_NOTHING, related_name = "accounts", blank = True, null = True)
    channels = models.ForeignKey("chat.Channel", models.DO_NOTHING, related_name = "accounts", blank = True,
                                 null = True)
    settings = models.OneToOneField("chat.Setting", models.CASCADE, related_name = "accounts", blank = True,
                                    null = True)


class Setting(AbstractBaseModel):
    LANGUAGE_CHOICES = [
        ("ru", "Russian"),
        ("en", "English")
    ]
    languages = models.CharField(max_length = 2, choices = LANGUAGE_CHOICES, default = "en")

    def __str__(self) -> str:
        return "Settings"


class Chat(AbstractBaseModel):
    messages = models.ForeignKey("chat.ChatMessage", models.DO_NOTHING, related_name = "chats")
    notifications = models.BooleanField(default = True)

    def __str__(self) -> str:
        return self.messages


class Group(AbstractBaseModel):
    name = models.CharField(max_length = 60)
    descriptions = models.CharField(max_length = 180, blank = True, null = True)
    author = models.ForeignKey("users.UserProfile", models.CASCADE, related_name = "author_groups")
    subscribers = models.ManyToManyField("users.UserProfile", related_name = "subscriber_groups", blank = True)
    messages = models.ForeignKey("chat.GroupMessage", models.CASCADE, related_name = "groups", blank = True,
                                 null = True)
    notifications = models.BooleanField(default = True)

    def __str__(self) -> str:
        return self.name

    def leave_group(self, author):
        self.subscribers.remove(author)

    def join_group(self, author):
        self.subscribers.add(author)

    def subscribers_count(self):
        return len(self.subscribers.all())


class Channel(AbstractBaseModel):
    name = models.CharField(max_length = 60)
    descriptions = models.CharField(max_length = 180)
    author = models.ForeignKey("users.UserProfile", models.DO_NOTHING, related_name = "author_channels")
    subscribers = models.ManyToManyField("users.UserProfile", related_name = "subscriber_channels", blank = True)
    messages = models.ForeignKey("chat.ChannelMessage", models.CASCADE, related_name = "channels", blank = True,
                                 null = True)
    notifications = models.BooleanField(default = True)

    def __str__(self) -> str:
        return self.name

    def leave_channel(self, subscriber):
        self.subscribers.remove(subscriber)

    def join_channel(self, subscriber):
        self.subscribers.add(subscriber)

    def subscribers_count(self):
        return len(self.subscribers.all())


class ChatMessage(AbstractBaseModel):
    author_from = models.ForeignKey("users.UserProfile", related_name = "chat_messages_sent",
                                    on_delete = models.CASCADE)
    author_to = models.ForeignKey("users.UserProfile", related_name = "chat_messages_received",
                                  on_delete = models.CASCADE)

    message_text = models.TextField()
    message_file = models.FileField(upload_to = "chats/chats/messages/files/", blank = True, null = True)
    message_image = models.ImageField(upload_to = "chats/chats/messages/images/", blank = True, null = True)

    def __str__(self) -> str:
        return f"{self.author_from} -> {self.author_to}"

    def save(self, *args, **kwargs):
        if self.message_text or self.message_file or self.message_image:
            return super().save(*args, **kwargs)
        else:
            raise ValidationError("now message error!")


class GroupMessage(AbstractBaseModel):
    author_from = models.ForeignKey("users.UserProfile", models.CASCADE, related_name = "group_messages_send")
    author_to = models.ForeignKey("users.UserProfile", models.CASCADE, related_name = "group_messages_recived",
                                  blank = True, null = True)

    message_text = models.TextField()
    message_file = models.FileField(upload_to = "chats/groups/messages/files/", blank = True, null = True)
    message_image = models.ImageField(upload_to = "chats/groups/messages/files/", blank = True, null = True)

    def __str__(self) -> str:
        return f"{self.author_from} -> {self.author_to}"

    def save(self, *args, **kwargs):
        if self.message_text or self.message_file or self.message_image:
            return super().save(*args, **kwargs)
        else:
            raise ValidationError("now message error!")


class ChannelMessage(AbstractBaseModel):
    author_from = models.ForeignKey("users.UserProfile", models.CASCADE, related_name = "channel_message_send")
    author_to = models.ForeignKey("users.UserProfile", models.CASCADE, related_name = "channel_message_recived",
                                  blank = True, null = True)

    message_text = models.TextField()
    message_file = models.FileField(upload_to = "chats/channel/messages/files/", blank = True, null = True)
    message_image = models.ImageField(upload_to = "chats/channel/messages/images/", blank = True, null = True)

    def __str__(self) -> str:
        return f"{self.author_from} -> {self.author_to}"

    def save(self, *args, **kwargs):
        if self.message_text or self.message_file or self.message_image:
            return super().save(*args, **kwargs)
        else:
            raise ValidationError("now message error!")
