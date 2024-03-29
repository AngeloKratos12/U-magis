# Generated by Django 4.1.3 on 2023-01-02 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0003_contactes_realisation_studentcompetences_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentFormation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idstudent', models.IntegerField()),
                ('ecole', models.CharField(max_length=20)),
                ('plusinfo', models.CharField(max_length=60)),
                ('date_debut', models.DateField()),
                ('date_fin', models.DateField()),
            ],
        ),
        migrations.RenameField(
            model_name='studentexperience',
            old_name='ecole',
            new_name='entreprise',
        ),
        migrations.RenameField(
            model_name='studentexperience',
            old_name='plusinfo',
            new_name='poste',
        ),
    ]
