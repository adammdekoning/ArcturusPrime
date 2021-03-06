# Generated by Django 3.1.5 on 2021-02-18 21:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('frontEnd', '0007_auto_20210218_2136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='athlete',
            name='email',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='athlete',
            name='squad',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='frontEnd.squad'),
        ),
        migrations.AlterField(
            model_name='result',
            name='boat_class',
            field=models.CharField(choices=[('2x', '2x'), ('4x+', '4x+'), ('4-', '4-'), ('8+', '8+'), ('4+', '4+'), ('1x', '1x'), ('2-', '2-'), ('4x', '4x')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='session_data',
            name='type',
            field=models.CharField(choices=[('running', 'running'), ('erg', 'erg'), ('swimming', 'swimming'), ('cycling', 'cycling'), ('cross training', 'cross training'), ('active recovery', 'active recovery'), ('rowing', 'rowing'), ('strength', 'strength')], max_length=256, null=True),
        ),
    ]
