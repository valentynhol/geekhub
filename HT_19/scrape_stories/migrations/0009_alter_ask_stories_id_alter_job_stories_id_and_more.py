# Generated by Django 4.0.1 on 2022-02-01 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scrape_stories', '0008_ask_stories_id_job_stories_id_new_stories_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ask',
            name='stories_id',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='job',
            name='stories_id',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='new',
            name='stories_id',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='show',
            name='stories_id',
            field=models.IntegerField(),
        ),
    ]
