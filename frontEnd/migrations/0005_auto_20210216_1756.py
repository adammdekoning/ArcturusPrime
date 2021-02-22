# Generated by Django 3.1.5 on 2021-02-16 17:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('frontEnd', '0004_coordinator'),
    ]

    operations = [
        migrations.CreateModel(
            name='Session_Data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('type', models.CharField(choices=[('erg', 'erg'), ('active recovery', 'active recovery'), ('cross training', 'cross training'), ('running', 'running'), ('swimming', 'swimming'), ('strength', 'strength'), ('rowing', 'rowing'), ('cycling', 'cycling')], max_length=256, null=True)),
                ('notes', models.CharField(max_length=256, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Squad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('distance', models.PositiveIntegerField()),
                ('time', models.TimeField()),
                ('rate', models.CharField(max_length=20, null=True)),
                ('notes', models.CharField(max_length=256, null=True)),
                ('boat_class', models.CharField(choices=[('2-', '2-'), ('4x', '4x'), ('2x', '2x'), ('1x', '1x'), ('8+', '8+'), ('4-', '4-'), ('4+', '4+'), ('4x+', '4x+')], max_length=10, null=True)),
                ('crew', models.ManyToManyField(to='frontEnd.Athlete')),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='frontEnd.session_data')),
            ],
        ),
        migrations.AlterField(
            model_name='athlete',
            name='squad',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='frontEnd.squad'),
        ),
    ]
