# Generated by Django 4.0.5 on 2022-06-29 00:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_alter_postmodel_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posttagmodel',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
