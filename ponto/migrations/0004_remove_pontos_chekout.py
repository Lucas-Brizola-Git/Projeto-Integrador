# Generated by Django 4.1.7 on 2023-03-27 22:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ponto', '0003_pontos_usuario'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pontos',
            name='chekout',
        ),
    ]