# Generated by Django 4.0.1 on 2022-01-29 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('scrape_stories', '0002_delete_categoryselector'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ask',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('by', models.CharField(max_length=100)),
                ('descendants', models.IntegerField()),
                ('stories_id', models.IntegerField()),
                ('score', models.IntegerField()),
                ('time', models.IntegerField()),
                ('title', models.CharField(max_length=150)),
                ('type', models.CharField(max_length=20)),
                ('text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('by', models.CharField(max_length=100)),
                ('stories_id', models.IntegerField()),
                ('score', models.IntegerField()),
                ('time', models.IntegerField()),
                ('title', models.CharField(max_length=150)),
                ('type', models.CharField(max_length=20)),
                ('url', models.URLField()),
                ('text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='New',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('by', models.CharField(max_length=100)),
                ('descendants', models.IntegerField()),
                ('stories_id', models.IntegerField()),
                ('score', models.IntegerField()),
                ('time', models.IntegerField()),
                ('title', models.CharField(max_length=150)),
                ('type', models.CharField(max_length=20)),
                ('url', models.URLField()),
                ('text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Show',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('by', models.CharField(max_length=100)),
                ('descendants', models.IntegerField()),
                ('stories_id', models.IntegerField()),
                ('score', models.IntegerField()),
                ('time', models.IntegerField()),
                ('title', models.CharField(max_length=150)),
                ('type', models.CharField(max_length=20)),
                ('url', models.URLField()),
                ('text', models.TextField()),
            ],
        ),
    ]