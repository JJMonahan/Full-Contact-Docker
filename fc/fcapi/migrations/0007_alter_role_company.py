# Generated by Django 4.2.6 on 2023-11-06 21:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fcapi', '0006_role_company_alter_company_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='role',
            name='company',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='fcapi.company'),
        ),
    ]
