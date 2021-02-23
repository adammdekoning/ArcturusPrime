# Generated by Django 3.1.5 on 2021-02-22 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontEnd', '0015_auto_20210222_1609'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coordinator',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='distance_data',
            name='boat_class',
            field=models.CharField(blank=True, choices=[('1x', '1x'), ('4x', '4x'), ('2x', '2x'), ('4+', '4+'), ('4x+', '4x+'), ('2-', '2-'), ('4-', '4-'), ('8+', '8+')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='distance_data',
            name='type',
            field=models.CharField(blank=True, choices=[('erg', 'erg'), ('active recovery', 'active recovery'), ('running', 'running'), ('bike', 'bike'), ('swimming', 'swimming'), ('rowing', 'rowing'), ('strength', 'strength'), ('cross training', 'cross training')], max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='result',
            name='boat_class',
            field=models.CharField(blank=True, choices=[('1x', '1x'), ('4x', '4x'), ('2x', '2x'), ('4+', '4+'), ('4x+', '4x+'), ('2-', '2-'), ('4-', '4-'), ('8+', '8+')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='session_data',
            name='type',
            field=models.CharField(blank=True, choices=[('erg', 'erg'), ('active recovery', 'active recovery'), ('running', 'running'), ('bike', 'bike'), ('swimming', 'swimming'), ('rowing', 'rowing'), ('strength', 'strength'), ('cross training', 'cross training')], max_length=256, null=True),
        ),
    ]