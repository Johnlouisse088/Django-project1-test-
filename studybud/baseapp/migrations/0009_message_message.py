# Generated by Django 5.0.3 on 2024-03-18 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baseapp', '0008_room_room'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='message',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
