# Generated by Django 2.0.2 on 2018-02-17 20:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('memories', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='memory',
            options={'verbose_name_plural': 'Memories'},
        ),
        migrations.RenameField(
            model_name='memory',
            old_name='storyistrue',
            new_name='story_is_true',
        ),
        migrations.RenameField(
            model_name='memory',
            old_name='whosfault',
            new_name='whos_fault',
        ),
    ]
