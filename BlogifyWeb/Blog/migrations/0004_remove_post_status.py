# Generated by Django 4.2.5 on 2023-09-24 12:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0003_alter_post_author_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='status',
        ),
    ]
