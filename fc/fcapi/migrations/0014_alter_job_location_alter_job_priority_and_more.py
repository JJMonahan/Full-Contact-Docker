# Generated by Django 4.2.7 on 2023-11-27 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fcapi', '0013_alter_job_priority'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='location',
            field=models.CharField(choices=[('0', 'Unknown'), ('1', 'Office'), ('2', 'Hybrid'), ('3', 'Remote')], default='Unknown', max_length=50),
        ),
        migrations.AlterField(
            model_name='job',
            name='priority',
            field=models.CharField(choices=[('0', 'Unknown'), ('1', 'Low'), ('2', 'Medium'), ('3', 'High'), ('4', 'Critical')], default='Unknown', max_length=50),
        ),
        migrations.AlterField(
            model_name='job',
            name='status',
            field=models.CharField(choices=[('0', 'Expressed Interest'), ('1', 'Applied'), ('2', 'Interviewing'), ('3', 'Pending Offer'), ('4', 'Rejection Received'), ('5', 'Withdrawn')], default='Unknown', max_length=50),
        ),
        migrations.AlterField(
            model_name='job',
            name='travel',
            field=models.CharField(choices=[('0', 'Unknown'), ('1', 'None'), ('2', 'Low'), ('3', 'Medium'), ('4', 'High')], default='Unknown', max_length=50),
        ),
    ]
