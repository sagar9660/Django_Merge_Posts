# Generated by Django 3.2.18 on 2023-03-10 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_user_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.CharField(choices=[('Others', 'Others'), ('Male', 'Male'), ('Female', 'Female')], default='Male', max_length=200),
        ),
    ]
