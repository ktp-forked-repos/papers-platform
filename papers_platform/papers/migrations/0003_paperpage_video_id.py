# Generated by Django 2.0.7 on 2018-07-21 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('papers', '0002_paperpage_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='paperpage',
            name='video_id',
            field=models.CharField(default='x', max_length=32),
            preserve_default=False,
        ),
    ]