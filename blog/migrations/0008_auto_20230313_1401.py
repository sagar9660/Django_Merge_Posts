# Generated by Django 3.2.18 on 2023-03-13 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20230313_1340'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tags',
            old_name='tag',
            new_name='name',
        ),
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.CharField(choices=[('Others', 'Others'), ('Male', 'Male'), ('Female', 'Female')], default='Male', max_length=200),
        ),
    ]
