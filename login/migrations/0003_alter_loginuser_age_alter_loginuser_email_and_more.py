# Generated by Django 4.0.3 on 2023-07-20 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_loginuser_age_loginuser_birth_day_loginuser_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loginuser',
            name='age',
            field=models.IntegerField(default=20, null='', verbose_name='나이'),
        ),
        migrations.AlterField(
            model_name='loginuser',
            name='email',
            field=models.EmailField(default=False, max_length=255, null='', verbose_name='이메일'),
        ),
        migrations.AlterField(
            model_name='loginuser',
            name='gender',
            field=models.CharField(default='male', max_length=10, null='', verbose_name='성별'),
        ),
        migrations.AlterField(
            model_name='loginuser',
            name='name',
            field=models.CharField(default=False, max_length=20, null='', verbose_name='이름'),
        ),
    ]
