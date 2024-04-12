from django.contrib import admin
from apps.chat.models import (
    Account,
    Chat,
    Group,
    Channel,
    ChatMessage,
    GroupMessage,
    ChannelMessage,
)


admin.site.register(Account)
admin.site.register(Chat)
admin.site.register(Group)
admin.site.register(Channel)
admin.site.register(ChatMessage)
admin.site.register(GroupMessage)
admin.site.register(ChannelMessage)
