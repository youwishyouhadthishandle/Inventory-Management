# Generated by Django 3.0.3 on 2020-02-21 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Equips', '0004_equipment_lastissued'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipment',
            name='lastIssued',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
