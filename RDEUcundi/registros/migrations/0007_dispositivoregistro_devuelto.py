# Generated by Django 2.0.4 on 2018-04-30 02:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registros', '0006_auto_20180429_2027'),
    ]

    operations = [
        migrations.AddField(
            model_name='dispositivoregistro',
            name='devuelto',
            field=models.BooleanField(default=0),
            preserve_default=False,
        ),
    ]
