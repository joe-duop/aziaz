# Generated by Django 3.1.1 on 2020-10-09 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0005_delete_video'),
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Video_title', models.CharField(max_length=250)),
                ('Video_artist', models.CharField(max_length=250)),
                ('Video_url', models.URLField()),
                ('Video_logo', models.ImageField(upload_to='Video_images')),
                ('Video_date_uploaded', models.DateField()),
            ],
        ),
    ]
