# Generated by Django 5.0.4 on 2024-04-11 19:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('chat', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='channel',
            name='subscribers',
            field=models.ManyToManyField(related_name='channels', to='users.userprofile'),
        ),
        migrations.AddField(
            model_name='account',
            name='channels',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='accounts', to='chat.channel'),
        ),
        migrations.AddField(
            model_name='channelmessage',
            name='author_from',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='channel_message_send', to='users.userprofile'),
        ),
        migrations.AddField(
            model_name='channelmessage',
            name='author_to',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='channel_message_recived', to='users.userprofile'),
        ),
        migrations.AddField(
            model_name='channel',
            name='messages',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='channels', to='chat.channelmessage'),
        ),
        migrations.AddField(
            model_name='account',
            name='chats',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='accounts', to='chat.chat'),
        ),
        migrations.AddField(
            model_name='chatmessage',
            name='author_from',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chat_messages_sent', to='users.userprofile'),
        ),
        migrations.AddField(
            model_name='chatmessage',
            name='author_to',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chat_messages_received', to='users.userprofile'),
        ),
        migrations.AddField(
            model_name='chat',
            name='messages',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='chats', to='chat.chatmessage'),
        ),
        migrations.AddField(
            model_name='group',
            name='author',
            field=models.ManyToManyField(related_name='groups', to='users.userprofile'),
        ),
        migrations.AddField(
            model_name='account',
            name='groups',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='accounts', to='chat.group'),
        ),
        migrations.AddField(
            model_name='groupmessage',
            name='author_from',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='group_messages_send', to='users.userprofile'),
        ),
        migrations.AddField(
            model_name='groupmessage',
            name='author_to',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='group_messages_recived', to='users.userprofile'),
        ),
        migrations.AddField(
            model_name='setting',
            name='my_profile',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='settings', to='users.userprofile'),
        ),
        migrations.AddField(
            model_name='account',
            name='settings',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='accounts', to='chat.setting'),
        ),
    ]
