# Generated by Django 4.1 on 2022-08-10 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ScubaDiving',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('location', models.CharField(max_length=150)),
                ('equipment', models.CharField(max_length=150)),
                ('description', models.TextField()),
                ('image', models.URLField(blank=True, null=True)),
            ],
        ),
    ]
