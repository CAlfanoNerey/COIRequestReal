# Generated by Django 3.0.3 on 2020-09-10 04:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_auto_20200909_2132'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipient',
            name='cost',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='recipient',
            name='employeenum',
            field=models.BigIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='recipient',
            name='rtype',
            field=models.CharField(blank=True, choices=[('Waiver of Subrogation', 'Waiver of Subrogation'), ('Alternate Employer Endorsement', 'Alternate Employer Endorsement')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='address2',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]