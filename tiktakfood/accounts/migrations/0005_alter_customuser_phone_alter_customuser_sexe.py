# Generated by Django 4.2.2 on 2023-08-18 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_customuser_birthday_customuser_sexe'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='phone',
            field=models.TextField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='sexe',
            field=models.CharField(default='M', max_length=10),
        ),
    ]
