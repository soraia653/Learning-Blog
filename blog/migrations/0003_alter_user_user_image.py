# Generated by Django 4.2.7 on 2023-11-18 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_user_user_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_image',
            field=models.ImageField(default='https://www.nicepng.com/png/full/933-9332131_profile-picture-default-png.png', upload_to='user_images/'),
        ),
    ]
