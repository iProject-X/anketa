# Generated by Django 3.0.5 on 2020-05-04 15:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='otvet',
            name='stimul',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stimuls', to='survey.Stimul_slov'),
        ),
    ]