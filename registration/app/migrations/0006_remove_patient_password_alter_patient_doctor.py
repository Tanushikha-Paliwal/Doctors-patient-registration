# Generated by Django 4.2.3 on 2023-08-23 04:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_patient'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='password',
        ),
        migrations.AlterField(
            model_name='patient',
            name='doctor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.doctors'),
        ),
    ]
