# Generated by Django 5.1.1 on 2024-10-02 08:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='complete',
            new_name='completado',
        ),
        migrations.RenameField(
            model_name='task',
            old_name='created',
            new_name='creado',
        ),
        migrations.RenameField(
            model_name='task',
            old_name='description',
            new_name='descripcion',
        ),
        migrations.RenameField(
            model_name='task',
            old_name='datecompleted',
            new_name='fechacompletado',
        ),
        migrations.RenameField(
            model_name='task',
            old_name='important',
            new_name='importante',
        ),
        migrations.RenameField(
            model_name='task',
            old_name='title',
            new_name='titulo',
        ),
        migrations.RenameField(
            model_name='task',
            old_name='user',
            new_name='usuario',
        ),
    ]
