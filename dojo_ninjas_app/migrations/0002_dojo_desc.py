# Generated by Django 3.1.5 on 2021-02-11 02:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dojo_ninjas_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dojo',
            name='desc',
            field=models.CharField(default='desc', max_length=50, verbose_name='dojo antiguo'),
            preserve_default=False,
        ),
    ]
