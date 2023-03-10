# Generated by Django 4.1.7 on 2023-03-14 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0004_task_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('slug', models.SlugField(null=True)),
            ],
        ),
        migrations.AddField(
            model_name='task',
            name='tag',
            field=models.ManyToManyField(to='todo.tag'),
        ),
    ]
