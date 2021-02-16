# Generated by Django 3.1.5 on 2021-02-15 23:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('frontEnd', '0002_auto_20210215_2307'),
    ]

    operations = [
        migrations.CreateModel(
            name='Club',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
            ],
        ),
        migrations.AlterField(
            model_name='athlete',
            name='club',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='frontEnd.club'),
        ),
        migrations.AlterField(
            model_name='coach',
            name='club',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='frontEnd.club'),
        ),
    ]