# Generated by Django 3.2.8 on 2021-11-02 03:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20211030_1710'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='address',
            field=models.CharField(help_text='Please Enter Your Residential Address', max_length=200),
        ),
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(help_text='Please Enter Your First Name', max_length=50),
        ),
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('Other', 'Other')], max_length=10),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(help_text='Please Enter Your Last/Given Name', max_length=50),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(help_text='Please Enter Your Phone number. eg: 01700000000', max_length=11, primary_key=True, serialize=False),
        ),
    ]
