# Generated by Django 4.2.5 on 2023-11-14 08:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0013_alter_post_photo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='photo',
            new_name='post_photo',
        ),
    ]
