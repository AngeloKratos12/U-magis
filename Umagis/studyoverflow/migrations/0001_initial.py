# Generated by Django 4.1.5 on 2023-01-09 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Question",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("question", models.CharField(max_length=200)),
                ("idUser", models.IntegerField()),
                ("about", models.CharField(max_length=20)),
                ("detail", models.TextField()),
                ("date", models.DateTimeField()),
            ],
        ),
    ]