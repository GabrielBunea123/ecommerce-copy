# Generated by Django 4.0.4 on 2022-08-10 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_profile_bookreviews'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.FileField(blank=True, default='https://ecommerce-101.s3.us-east-2.amazonaws.com/profile/userDefault.png', null=True, upload_to='profile/'),
        ),
    ]
