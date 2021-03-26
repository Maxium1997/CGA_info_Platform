# Generated by Django 3.1.4 on 2021-03-27 01:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('law', '0003_auto_20210325_1603'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['act', 'chapter', 'priority']},
        ),
        migrations.AddField(
            model_name='article',
            name='priority',
            field=models.PositiveIntegerField(default=1),
        ),
    ]