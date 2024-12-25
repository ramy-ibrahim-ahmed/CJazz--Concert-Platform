# Generated by Django 4.2.4 on 2023-08-10 22:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('capp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='party',
            name='plan',
        ),
        migrations.RemoveField(
            model_name='ticket',
            name='plan',
        ),
        migrations.AddField(
            model_name='ticket',
            name='plan',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='capp.plan', verbose_name='Ticket Type'),
        ),
    ]