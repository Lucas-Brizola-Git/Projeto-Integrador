# Generated by Django 4.1.7 on 2023-03-27 22:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
        ('ponto', '0002_alter_pontos_options_alter_pontos_chekin_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='pontos',
            name='usuario',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='usuarios.usuario'),
            preserve_default=False,
        ),
    ]
