# Generated by Django 3.0.7 on 2020-06-09 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20200609_2225'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='id_teacher_id',
            field=models.IntegerField(null=True),
        ),
    ]
