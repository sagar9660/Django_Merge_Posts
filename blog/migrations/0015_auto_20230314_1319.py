# Generated by Django 3.2.18 on 2023-03-14 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_auto_20230314_1211'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comments',
            options={'verbose_name_plural': 'Comments'},
        ),
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.CharField(choices=[('Others', 'Others'), ('Female', 'Female'), ('Male', 'Male')], default='Male', max_length=200),
        ),
    ]
