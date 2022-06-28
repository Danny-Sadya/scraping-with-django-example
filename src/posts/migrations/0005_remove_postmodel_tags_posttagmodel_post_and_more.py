# Generated by Django 4.0.5 on 2022-06-29 00:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_remove_postmodel_tags_postmodel_tags'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='postmodel',
            name='tags',
        ),
        migrations.AddField(
            model_name='posttagmodel',
            name='post',
            field=models.ManyToManyField(to='posts.postmodel'),
        ),
        migrations.AlterField(
            model_name='posttagmodel',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
