# Generated by Django 2.2.5 on 2019-09-25 02:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_post_cover'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='cover',
            field=models.ImageField(blank=True, upload_to='media/Post_image/'),
        ),
    ]