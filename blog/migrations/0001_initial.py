# Generated by Django 5.1.3 on 2024-11-30 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('date_posted', models.DateField(auto_now_add=True)),
                ('category', models.CharField(blank=True, max_length=100)),
                ('tags', models.CharField(blank=True, max_length=100)),
            ],
        ),
    ]
