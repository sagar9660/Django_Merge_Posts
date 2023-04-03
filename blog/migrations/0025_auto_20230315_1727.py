# Generated by Django 3.2.18 on 2023-03-15 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0024_auto_20230315_1725'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='image',
        ),
        migrations.AddField(
            model_name='post',
            name='featured',
            field=models.ImageField(blank=True, null=True, upload_to='featured/'),
        ),
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.CharField(choices=[('Others', 'Others'), ('Male', 'Male'), ('Female', 'Female')], default='Male', max_length=200),
        ),
    ]
