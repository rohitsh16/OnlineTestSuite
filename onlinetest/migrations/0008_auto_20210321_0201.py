# Generated by Django 2.2.10 on 2021-03-20 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlinetest', '0007_question_audio'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='navbar_theme',
            field=models.CharField(default='', help_text='color code for question theme', max_length=100),
        ),
        migrations.AddField(
            model_name='event',
            name='question_theme',
            field=models.CharField(default='', help_text='color code for question theme', max_length=100),
        ),
    ]
