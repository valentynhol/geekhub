# Generated by Django 4.0.1 on 2022-01-30 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scrape_stories', '0005_alter_ask_by_alter_ask_score_alter_ask_text_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ask',
            name='url',
        ),
        migrations.AddField(
            model_name='ask',
            name='descendants',
            field=models.IntegerField(default=None),
        ),
        migrations.AddField(
            model_name='new',
            name='descendants',
            field=models.IntegerField(default=None),
        ),
        migrations.AddField(
            model_name='show',
            name='descendants',
            field=models.IntegerField(default=None),
        ),
    ]
