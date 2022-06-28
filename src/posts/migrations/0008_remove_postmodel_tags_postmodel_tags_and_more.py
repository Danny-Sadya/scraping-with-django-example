# Generated by Django 4.0.5 on 2022-06-29 01:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0007_remove_posttagmodel_post_postmodel_tags'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='postmodel',
            name='tags',
        ),
        migrations.AddField(
            model_name='postmodel',
            name='tags',
            field=models.CharField(blank=True, max_length=2048, null=True),
        ),
        migrations.DeleteModel(
            name='PostTagModel',
        ),
    ]
