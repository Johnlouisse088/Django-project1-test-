# Generated by Django 5.0.3 on 2024-03-18 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baseapp', '0004_rename_topics_topic'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='name',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
