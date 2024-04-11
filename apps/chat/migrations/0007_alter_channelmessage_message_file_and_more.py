# Generated by Django 5.0.4 on 2024-04-11 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0006_channel_author_group_subscribers_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='channelmessage',
            name='message_file',
            field=models.FileField(blank=True, null=True, upload_to='chats/channel/messages/files/'),
        ),
        migrations.AlterField(
            model_name='channelmessage',
            name='message_image',
            field=models.ImageField(blank=True, null=True, upload_to='chats/channel/messages/images/'),
        ),
        migrations.AlterField(
            model_name='chatmessage',
            name='message_file',
            field=models.FileField(blank=True, null=True, upload_to='chats/chats/messages/files/'),
        ),
        migrations.AlterField(
            model_name='chatmessage',
            name='message_image',
            field=models.ImageField(blank=True, null=True, upload_to='chats/chats/messages/images/'),
        ),
        migrations.AlterField(
            model_name='groupmessage',
            name='message_file',
            field=models.FileField(blank=True, null=True, upload_to='chats/groups/messages/files/'),
        ),
        migrations.AlterField(
            model_name='groupmessage',
            name='message_image',
            field=models.ImageField(blank=True, null=True, upload_to='chats/groups/messages/files/'),
        ),
    ]
