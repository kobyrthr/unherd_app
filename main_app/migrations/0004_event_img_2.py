# Generated by Django 4.0.3 on 2022-04-23 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_rsvp'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='img_2',
            field=models.ImageField(default='', upload_to='images/'),
            preserve_default=False,
        ),
    ]