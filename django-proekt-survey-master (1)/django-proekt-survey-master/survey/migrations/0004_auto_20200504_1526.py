# Generated by Django 3.0.5 on 2020-05-04 15:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0003_auto_20200504_1520'),
    ]

    operations = [
        migrations.AlterField(
            model_name='otvet',
            name='stimul',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stimuls', to='survey.Stimul_slov'),
        ),
    ]
