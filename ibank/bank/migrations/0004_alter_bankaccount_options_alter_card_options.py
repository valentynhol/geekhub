# Generated by Django 4.0.1 on 2022-04-20 17:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0003_alter_card_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bankaccount',
            options={'verbose_name': 'банківський рахунок', 'verbose_name_plural': 'банківські рахунки'},
        ),
        migrations.AlterModelOptions(
            name='card',
            options={'verbose_name': 'картка', 'verbose_name_plural': 'картки'},
        ),
    ]
