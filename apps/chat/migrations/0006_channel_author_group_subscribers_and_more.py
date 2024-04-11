# Generated by Django 5.0.4 on 2024-04-11 19:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0005_alter_group_messages'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='channel',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, related_name='author_channels', to='users.userprofile'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='group',
            name='subscribers',
            field=models.ManyToManyField(blank=True, related_name='subscriber_groups', to='users.userprofile'),
        ),
        migrations.AlterField(
            model_name='channel',
            name='messages',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='channels', to='chat.channelmessage'),
        ),
        migrations.AlterField(
            model_name='channel',
            name='subscribers',
            field=models.ManyToManyField(blank=True, related_name='subscriber_channels', to='users.userprofile'),
        ),
        migrations.RemoveField(
            model_name='group',
            name='author',
        ),
        migrations.AlterField(
            model_name='group',
            name='messages',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='groups', to='chat.groupmessage'),
        ),
        migrations.AddField(
            model_name='group',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='author_groups', to='users.userprofile'),
            preserve_default=False,
        ),
    ]
