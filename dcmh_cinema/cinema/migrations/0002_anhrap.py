# Generated by Django 2.2.5 on 2019-10-25 12:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cinema', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnhRap',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('anhRap_anh', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cinema.Anh')),
                ('anhRap_rap', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cinema.Rap')),
            ],
        ),
    ]
