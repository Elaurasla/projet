# Generated by Django 3.1.2 on 2022-05-10 12:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CourriersApp', '0003_remove_courrier_supprimer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bureau',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='CourrierDepart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num', models.PositiveIntegerField()),
                ('date', models.DateField()),
                ('date_emission', models.DateField()),
                ('reference', models.TextField(blank=True)),
                ('origine', models.CharField(max_length=100)),
                ('objet', models.TextField(blank=True)),
                ('bureau', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CourriersApp.bureau')),
            ],
        ),
    ]
